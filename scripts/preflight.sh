#!/usr/bin/env bash
# 渲染前预检：先出 3 帧静帧，再判空帧。
# 用法（在 Remotion 工程根目录执行）：
#   bash preflight.sh src/index.ts <CompositionId> 0 30 90
# 通过才整片渲染；不通过 30 秒就能发现，不必用 10 分钟去发现。
set -uo pipefail

entry="${1:?用法: preflight.sh <entry> <compositionId> [frames...]}"
comp="${2:?缺 compositionId}"
shift 2 || true
frames=("$@")
if [ "${#frames[@]}" -eq 0 ]; then frames=(0 30 90); fi

[ -f "$entry" ] || { echo "✗ entry 不存在: $entry（请在工程根目录执行）" >&2; exit 1; }
mkdir -p out

fail=0
imgs=()
for f in "${frames[@]}"; do
  out="out/preflight_$f.png"
  if ! npx remotion still "$entry" "$comp" "$out" --frame="$f" --concurrency=1 --log=error >/dev/null 2>&1; then
    echo "✗ frame $f 渲染失败（多半是并发默认值或 TS 编译错）"
    echo "  先试：--concurrency=1；再查 composition 是否已注册"
    fail=1
    continue
  fi
  # 本机 ffmpeg 4.4 的 signalstats 没有 YSTD，用亮度极差 YMAX-YMIN 判空帧
  stats=$(ffmpeg -v error -i "$out" -vf "signalstats,metadata=print:file=-" -f null - 2>/dev/null)
  yavg=$(echo "$stats" | grep -m1 "signalstats.YAVG=" | sed 's/.*=//')
  ymin=$(echo "$stats" | grep -m1 "signalstats.YMIN=" | sed 's/.*=//')
  ymax=$(echo "$stats" | grep -m1 "signalstats.YMAX=" | sed 's/.*=//')
  verdict=$(python3 -c "print('EMPTY' if (float('${ymax:-0}') - float('${ymin:-0}')) < 12 else 'OK')" 2>/dev/null || echo CHECK)
  echo "frame $f -> $out  YAVG=${yavg:-?} 亮度极差=$(( ${ymax:-0} - ${ymin:-0} ))  [${verdict}]"
  [ "$verdict" = "EMPTY" ] && { echo "  ⚠ 疑似空帧/纯色：检查首帧是否真的落了内容、图层是否被 mask 掉、数据是否为空"; fail=1; }
  imgs+=("$out")
done

if [ "${#imgs[@]}" -gt 1 ] && command -v ffmpeg >/dev/null 2>&1; then
  n=${#imgs[@]}
  inputs=(); filt=""
  for ((i=0;i<n;i++)); do inputs+=(-i "${imgs[$i]}"); filt+="[$i:v]scale=-2:560[v$i];"; done
  for ((i=0;i<n;i++)); do filt+="[v$i]"; done
  filt+="hstack=inputs=$n"
  ffmpeg -v error -y "${inputs[@]}" -filter_complex "$filt" out/preflight_sheet.png
  echo "✓ 预检联系表: out/preflight_sheet.png"
fi

if [ "$fail" -eq 0 ]; then
  echo "✓ 预检通过，可以整片渲染"
else
  echo "✗ 预检未通过，先修再渲染"
fi
exit "$fail"
