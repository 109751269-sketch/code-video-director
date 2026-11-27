#!/usr/bin/env python3
"""镜头表路由：把每个镜头分给最合适的代码渲染引擎。

用法：
  python3 route.py shots.json      # 读镜头表，出路由表与命令
  python3 route.py --test          # 跑内置 14 条历史用例做自检

镜头表格式：
{
  "title": "示例片",
  "canvas": "1080x1920",
  "fps": 30,
  "shots": [
    {"id": 1, "start": 0, "dur": 3, "kind": "ui",
     "motion": "cut", "text_heavy": true,
     "layout_precise": false, "note": "大字提问"}
  ]
}

labels: kind ∈ ui|data|scene|mixed ; motion ∈ cut|grow|loop|follow
"""
import json
import sys

KINDS = {"ui", "data", "scene", "mixed"}
MOTIONS = {"cut", "grow", "loop", "follow"}

ENGINE_HINT = {
    "shotcraft": "从 124 张卡里选构图最接近的一张，只改卡内文案/配色/数字",
    "iart": "light tier 单 HTML + draw(t)，URL 必须带 ?t= 求帧",
    "hyperframes": "HTML+CSS+GSAP，整页重排与连续运镜，自建 seek(t) 契约后逐帧截图",
}


def route_shot(shot):
    kind = shot.get("kind", "mixed")
    motion = shot.get("motion", "cut")
    dur = float(shot.get("dur", 3))
    lp = bool(shot.get("layout_precise", False))

    if kind not in KINDS:
        raise ValueError(f"shot {shot.get('id')}: 非法 kind={kind}")
    if motion not in MOTIONS:
        raise ValueError(f"shot {shot.get('id')}: 非法 motion={motion}")

    # 1 连续运镜（跟拍）：卡库没有跟拍卡，交给 hyperframes 的连续时间轴
    if motion == "follow":
        return "hyperframes"
    # 2 数据类连续生长/循环：draw(t) 就是时间函数，iart 最合适
    if kind == "data" and motion in ("grow", "loop"):
        return "iart"
    # 3 长时间非数据生长（版式推移/卡片膨胀）：整页重排给 hyperframes
    if motion == "grow" and dur > 6 and kind in ("ui", "mixed"):
        return "hyperframes"
    # 4 跳切 + UI：套现成卡（布局精确度只影响卡内微调，不改引擎）
    if motion == "cut" and kind == "ui":
        return "shotcraft"
    # 5 长镜头场景 / 网页级动效
    if kind == "scene" and dur > 6:
        return "hyperframes"
    if motion == "loop":
        return "hyperframes"
    # 6 兜底
    return "shotcraft"


def run(spec):
    shots = spec.get("shots") or []
    if not shots:
        raise ValueError("镜头表为空")
    rows = []
    for s in shots:
        engine = route_shot(s)
        rows.append({
            "id": s.get("id", len(rows) + 1),
            "start": s.get("start", 0),
            "dur": s.get("dur", 3),
            "kind": s.get("kind", "mixed"),
            "motion": s.get("motion", "cut"),
            "engine": engine,
            "note": s.get("note", ""),
        })

    canvas = spec.get("canvas", "1080x1920")
    fps = int(spec.get("fps", 30))
    total = max((r["start"] + r["dur"] for r in rows), default=0)

    print(f"# {spec.get('title', '未命名')}  {canvas} @{fps}fps  约 {total:g}s / {int(total * fps)} 帧\n")
    print("| # | 时间 | 时长 | kind | motion | 引擎 | 说明 |")
    print("|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['id']} | {r['start']:g}s | {r['dur']:g}s | {r['kind']} | {r['motion']} | **{r['engine']}** | {r['note']} |")

    counts = {}
    for r in rows:
        counts[r["engine"]] = counts.get(r["engine"], 0) + 1
    print("\n## 引擎用量")
    for e, c in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"- {e}: {c} 个镜头 — {ENGINE_HINT[e]}")

    if len(counts) > 1:
        print("\n## 编排建议")
        if "shotcraft" in counts:
            print("- 以 shotcraft 工程为主时间轴，其余引擎产物转 PNG 序列当素材层喂进去（避免 ffmpeg 拼接的色差与字体差异）")
        if "hyperframes" in counts:
            print("- hyperframes 只做独立片头/片尾，不要混进主时间轴")
        if "iart" in counts:
            print("- iart 逐帧截图 300 帧约 2 分钟，适合先出图确认再进主时间轴")
    else:
        print("\n## 编排建议\n- 单一引擎，直接整体渲染即可，不要再拆")
    return rows


CASES = [
    {
        "name": "案例1 信息流卡片 15s",
        "spec": {"title": "信息流卡片", "canvas": "1920x1080", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 3, "kind": "ui", "motion": "cut", "text_heavy": True},
            {"id": 2, "start": 3, "dur": 4, "kind": "ui", "motion": "cut", "text_heavy": True},
            {"id": 3, "start": 7, "dur": 4, "kind": "data", "motion": "cut", "text_heavy": False},
            {"id": 4, "start": 11, "dur": 4, "kind": "ui", "motion": "cut", "text_heavy": True},
        ]},
        "expect": ["shotcraft", "shotcraft", "shotcraft", "shotcraft"],
    },
    {
        "name": "案例2 BNB 曲线跟拍",
        "spec": {"title": "BNB 复刻", "canvas": "1920x1080", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 15, "kind": "data", "motion": "follow", "text_heavy": False},
        ]},
        "expect": ["hyperframes"],
    },
    {
        "name": "案例3 竖屏 AI 测评 30s",
        "spec": {"title": "竖屏复刻", "canvas": "1080x1920", "fps": 30, "shots": [
            {"id": i + 1, "start": i * 4.3, "dur": 4.3, "kind": "ui", "motion": "cut",
             "text_heavy": True, "layout_precise": True, "note": n}
            for i, n in enumerate(["开场", "日历卡", "榜单卡", "天平", "三人", "领奖台", "收尾"])
        ]},
        "expect": ["shotcraft"] * 7,
    },
    {
        "name": "案例4 三库横向实测",
        "spec": {"title": "横向实测", "canvas": "mix", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 3, "kind": "ui", "motion": "cut", "text_heavy": True},
            {"id": 2, "start": 3, "dur": 4, "kind": "data", "motion": "loop", "text_heavy": False},
            {"id": 3, "start": 7, "dur": 8, "kind": "scene", "motion": "grow", "text_heavy": False},
        ]},
        "expect": ["shotcraft", "iart", "hyperframes"],
    },
    # ---- 边界用例：覆盖每个判定分支与相邻阈值 ----
    {
        "name": "边界5 长 UI 生长 8s",
        "spec": {"title": "卡片膨胀", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 8, "kind": "ui", "motion": "grow", "text_heavy": False},
        ]},
        "expect": ["hyperframes"],
    },
    {
        "name": "边界6 短数据柱状 3s",
        "spec": {"title": "柱状生长", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 3, "kind": "data", "motion": "grow", "text_heavy": False},
        ]},
        "expect": ["iart"],
    },
    {
        "name": "边界7 场景快切 4s",
        "spec": {"title": "场景切", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 4, "kind": "scene", "motion": "cut", "text_heavy": False},
        ]},
        "expect": ["shotcraft"],
    },
    {
        "name": "边界8 混合长镜头 7s",
        "spec": {"title": "混合推移", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 7, "kind": "mixed", "motion": "grow", "text_heavy": False},
        ]},
        "expect": ["hyperframes"],
    },
    {
        "name": "边界9 循环背景 5s",
        "spec": {"title": "循环底纹", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 5, "kind": "scene", "motion": "loop", "text_heavy": False},
        ]},
        "expect": ["hyperframes"],
    },
    {
        "name": "边界10 短数据数字滚动 2s",
        "spec": {"title": "分数滚动", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 2, "kind": "data", "motion": "cut", "text_heavy": True},
        ]},
        "expect": ["shotcraft"],
    },
    {
        "name": "边界11 UI 跟拍 3s",
        "spec": {"title": "卡片跟拍", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 3, "kind": "ui", "motion": "follow", "text_heavy": False},
        ]},
        "expect": ["hyperframes"],
    },
    {
        "name": "边界12 超短标点 1s",
        "spec": {"title": "一秒卡点", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 1, "kind": "ui", "motion": "cut", "text_heavy": True},
        ]},
        "expect": ["shotcraft"],
    },
    {
        "name": "边界13 5s 数据生长（阈值下沿）",
        "spec": {"title": "阈值", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 5, "kind": "data", "motion": "grow", "text_heavy": False},
        ]},
        "expect": ["iart"],
    },
    {
        "name": "边界14 5.5s 数据生长（长镜头仍归 iart）",
        "spec": {"title": "阈值", "fps": 30, "shots": [
            {"id": 1, "start": 0, "dur": 5.5, "kind": "data", "motion": "grow", "text_heavy": False},
        ]},
        "expect": ["iart"],
    },
]


def test():
    failed = 0
    for c in CASES:
        rows = run(c["spec"])
        got = [r["engine"] for r in rows]
        ok = got == c["expect"]
        failed += 0 if ok else 1
        print(f"\n=> {c['name']}: {'PASS' if ok else 'FAIL'}  期望 {c['expect']} 实际 {got}\n")
    print(f"自检结果：{len(CASES) - failed}/{len(CASES)} 通过")
    return 1 if failed else 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    if sys.argv[1] == "--test":
        return test()
    with open(sys.argv[1], encoding="utf-8") as f:
        spec = json.load(f)
    run(spec)
    return 0


if __name__ == "__main__":
    sys.exit(main())
