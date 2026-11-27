#!/usr/bin/env bash
# 交付前核查：规格 + 关键帧联系表
# 用法：bash verify_video.sh <mp4> [t1 t2 t3 ...]
# 不给时间点则自动取 10% / 50% / 90% 三个位置
set -euo pipefail

mp4="${1:?用法: verify_video.sh <mp4> [t1 t2 t3 ...]}"
shift || true
[ -f "$mp4" ] || { echo "✗ 文件不存在: $mp4" >&2; exit 1; }

echo "== 规格 =="
ffprobe -v error -select_streams v:0 \
  -show_entries stream=codec_name,width,height,r_frame_rate,nb_frames \
  -of default=nw=1 "$mp4"

dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$mp4")
fps=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$mp4")
nf=$(ffprobe -v error -select_streams v:0 -count_frames -show_entries stream=nb_read_frames -of csv=p=0 "$mp4")

echo "时长 ${dur}s | 帧率 ${fps} | 实读帧数 ${nf}"
python3 - "$dur" "$fps" "$nf" <<'PY'
import sys
dur, fps_s, nf = float(sys.argv[1]), sys.argv[2], int(sys.argv[3])
num, den = (fps_s.split('/') + ['1'])[:2]
fps = float(num) / float(den)
expect = round(dur * fps)
gap = abs(expect - nf)
print(f"按 {fps:g}fps 推算应有 {expect} 帧，实读 {nf} 帧，差 {gap} 帧")
print("✓ 帧数一致" if gap <= 2 else f"⚠ 帧数不一致（差 {gap}），可能是渲染中断留下的半成品")
PY

workdir=$(mktemp -d)
trap 'rm -rf "$workdir"' EXIT

if [ "$#" -gt 0 ]; then
  times=("$@")
else
  times=$(python3 - "$dur" <<'PY'
import sys
d = float(sys.argv[1])
print(" ".join(f"{d*r:.2f}" for r in (0.1, 0.5, 0.9)))
PY
)
  # shellcheck disable=SC2207
  times=($(echo "$times"))
fi

echo "== 抽帧 =="
inputs=()
for i in "${!times[@]}"; do
  t="${times[$i]}"
  out="$workdir/f$i.png"
  ffmpeg -v error -ss "$t" -i "$mp4" -frames:v 1 -q:v 2 "$out"
  echo "t=${t}s -> $out"
  inputs+=(-i "$out")
done

base="${mp4%.*}"
n=${#times[@]}
if [ "$n" -eq 1 ]; then
  cp "$workdir/f0.png" "${base}-check.png"
else
  filt=""
  for ((i=0;i<n;i++)); do filt+="[$i:v]scale=-2:640[v$i];"; done
  for ((i=0;i<n;i++)); do filt+="[v$i]"; done
  filt+="hstack=inputs=$n"
  ffmpeg -v error -y "${inputs[@]}" -filter_complex "$filt" "${base}-check.png"
fi
echo "✓ 联系表: ${base}-check.png"
