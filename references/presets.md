# 预设（默认值，覆盖前先说明理由）

## 画幅

| 用途 | 分辨率 | 比例 | 备注 |
|---|---|---|---|
| 抖音/视频号竖屏 | 1080×1920 | 9:16 | 默认 |
| 复刻 4:3 参考片 | 1440×1080 | 4:3 | 参考片实测接近这个比例时用这个，不要硬拉成竖屏 |
| B 站/横屏演示 | 1920×1080 | 16:9 | |
| 方图/朋友圈 | 1080×1080 | 1:1 | |

帧率固定 30fps，总帧数 = 时长 × 30。不要用 25 或 60，除非原片是。

## 色彩

- 主题：`midnight`（深底 + 冷白字 + 单一强调色），科技感、不廉价
- 强调色只用一到两个：主色 + 高亮色（数据下跌/警示才用暖红）
- 渐变透明度不低于 0.06，避免出现色带
- 光效：`boxShadow` 或径向渐变模拟，不要叠三层以上发光，会糊

## 字体与字幕

```tsx
fontFamily: '"Noto Sans CJK SC","Noto Sans CJK TC",sans-serif'
```

- 中文硬字幕：字号按画幅高换算（1080×1920 用 44–50px），`WebkitTextStroke: '1px rgba(255,255,255,0.9)'` + 轻微白色 textShadow，保证浅底也能读
- 单行不超过 16 字，超出就拆成两句错时入场，不要自动换行
- 字幕基线距底 90–120px（竖屏），避开平台 UI

## 命名与目录

```
复刻-<主题>-<版本>.mp4        例：复刻BNB-15秒-v2-笔尖跟拍.mp4
对比-<场景>-<秒>.png          例：对比-竖屏19秒.png
源码/<片名>.tsx | .html
```

工作副本放 `/home/user/work/<engine>/`，交付物放项目目录，源码一律复制一份进 `源码/`。

## 命令模板

```bash
# shotcraft / Remotion（--concurrency 必须显式给，≤300 帧可 2，整片用 1）
cd <project>/template && npx remotion render src/index.ts <CompId> out/x.mp4 --concurrency=1
# still 也要带并发参数：npx remotion still src/index.ts <CompId> out/a.png --frame=0 --concurrency=1

# 抽帧核对
ffmpeg -ss 3.2 -i out/x.mp4 -frames:v 1 -q:v 2 chk.png

# 对比图（左原片右复刻，先统一高度）
ffmpeg -i a.png -i b.png -filter_complex "[0:v]scale=-2:720[l];[1:v]scale=-2:720[r];[l][r]hstack" cmp.png
```

## 复刻边界话术

先给三档结论，再动手：

- **能复刻**：几何、运动逻辑、节奏、文字内容
- **只能近似**：材质（笔触/纸纹）、光斑、真人、IP 角色美术
- **不能复刻**：原片专有字体、平台 UI、需要原始素材的画面

报告保真度用"运动机制 X% / 整体观感 Y%"两段式，并点名卡在哪一环，不要给一个笼统分数。

## 交付单 SPEC.md（工程根目录，六行写死）

```markdown
# SPEC
- 画幅：1920x1080
- 帧率：30
- 总帧数：1400
- composition：SkillsIntro
- 输出：out/skills_intro.mp4
- 数据源：src/data/skills.json
```

渲染命令从这里取参数，不要凭记忆；改了任何一项，先改 SPEC 再动手。

## 数据单一来源

```json
// src/data/<主题>.json —— 屏幕上每个数字的唯一来源
{ "bars": [{ "label": "1月", "value": 38 }, { "label": "3月", "value": 52 }] }
```

- composition `import data from '../data/xxx.json'`，柱子高度、字幕里的数字、榜单分数全部读同一个字段
- 禁止在 JSX 里直接写 `74`、`62%` 这类字面量：改数据时必然漏改一处
- 渲染前预检时抽一个数字与 JSON 对账

## 各引擎的"默认值陷阱"

| 引擎 | 默认 | 后果 |
|---|---|---|
| Remotion | 不指定 composition 会弹交互选择器，非交互终端直接失败 | CI/后台渲染必挂 |
| Remotion | 并发默认按宿主机核数算（本机算成 4） | 超过 2 核直接拒渲，`still` 同样会挂 |
| hyperframes | 默认时长只有 30 帧（1 秒） | 片头在 1 秒处断掉，看起来像"只渲了一帧" |
| iart | 默认进入 rAF 自播放 | 手动求帧被覆盖 |
