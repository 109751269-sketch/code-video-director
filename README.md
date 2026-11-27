<!-- 本文件面向人类读者（GitHub 首页、交接说明）。Agent 不读它，运行规则以 SKILL.md 为准。 -->

# 代码视频导演 · code-video-director

用代码逐帧渲染做视频（video-as-code），不调用任何视频生成模型。给一个专题，先立六位叙事骨架，再按位从 124 张镜头卡里选卡，最后决定每个镜头交给哪个引擎。

## 三个引擎

| 引擎 | 本质 | 做什么 | 不做 |
|---|---|---|---|
| **shotcraft** | React + Remotion，124 张镜头配方卡 | 信息流短视频、UI 卡片、榜单、快节奏竖屏、中文字幕 | 单镜头长时间连续生长、曲线跟拍、真人 |
| **iart（light tier）** | 单个 HTML + Canvas `draw(t)` 纯函数 | 曲线 / 柱状 / 粒子，一张画面讲透一件事，可独立分发 | 多镜头叙事、复杂排版 |
| **hyperframes** | HTML + CSS + GSAP → headless Chrome | 复用现成网页、整页排版、连续运镜、SVG 滤镜与循环动效 | 官方渲染路径不可靠，需自建 seek |

没有"自己写一套组件"这条路。卡对不上构图时：换同族卡 → 改卡内文案/配色/坐标 → 整页交给 hyperframes。

## 一条专题怎么走

```bash
# 1 选卡：六位骨架 × 每位的三张候选
python3 scripts/pick_cards.py --topic "AI 订阅套餐横评，价格与额度对比"
python3 scripts/pick_cards.py --topic "..." --json > shots.json

# 2 人工定卡后，路由到引擎
python3 scripts/route.py shots.json

# 3 渲染前先出 3 帧自检，别直接渲整片
bash scripts/preflight.sh src/index.ts <CompositionId> 0 470 801

# 4 出片后核查规格与关键帧
bash scripts/verify_video.sh out/xxx.mp4 0.5 3.2 8.0
```

六位骨架：钩子（0–4s）→ 定义（4–9s）→ 证据（9–17s）→ 对比（17–25s）→ 结论（25–31s）→ 收尾（31–36s）。专题没有某一位就直接删，别硬凑；需要过渡时插一张 `bridge` 转场卡。

## 目录

```
SKILL.md                 运行规则：四道闸、三引擎路由、预检与交付
references/
  cards-index.md        124 张卡的人读表（卡名/类别/时长/能量/版式/适合位）
  cards-index.json      同内容机器读版，pick_cards.py 直接吃
  routing.md            镜头标签定义、完整路由表、混合编排
  pitfalls.md           各引擎启动命令与已验证的崩溃修复（2 核/4GB 必读）
  presets.md            画幅、配色、字体、字幕、命名、渲染命令模板
  cases.md              四条真实案例的路由结果与复刻保真度
scripts/
  pick_cards.py         专题 → 六位候选卡 + shots 骨架
  route.py              镜头表 → 引擎，含 14 条自检用例（--test）
  build_cards_index.py  卡库变动后重建索引
  preflight.sh          3 帧预检 + 空帧判定 + 联系表
  verify_video.sh       交付核查：规格 + 关键帧联系表
agents/                 豆包 / OpenAI 的 display_name 与触发策略
```

## 依赖

- Python 3（无第三方库）；Node 22 + Remotion 4.0.484 工程（shotcraft 侧）
- ffmpeg / ffprobe（抽帧与规格核查）
- Chrome + puppeteer-core（hyperframes 自建 seek 渲染）

## 已知限制

- 选卡打分是"关键词 × 位亲和 × 能量 × 时长"的规则，不做语义理解；脚本只负责把候选排得有依据，**终选仍需人拍板**。
- `cards-index` 是卡库快照。卡库新增/改名/改时长后跑 `scripts/build_cards_index.py --library <library.json>` 重建。
- `route.py --test` 的 14 条用例覆盖的是路由边界，不覆盖画面审美。
- hyperframes 官方渲染路径会出 0 帧，必须自建 `seek(t)` 逐帧截图；且 `code-slice-hero`、`chromatic-radial-split` 在本机 seek 无效，`aurora` 需 WebGPU。
- iart 体系只有规格与 starter，没有预置成片样片。
- 文档里的命令用 `python3` / `bash`；Windows 环境换成 `python` / PowerShell。

## 安装

把这个文件夹放到技能目录即可：

- 豆包 / 本地 agent：`~/.agents/skills/code-video-director`（Windows 为 `C:\Users\<用户>\.agents\skills\code-video-director`）
- 或工作区：`<workspace>/.user_skills/code-video-director`

GitHub 镜像：https://github.com/109751269-sketch/code-video-director
