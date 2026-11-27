# 路由：从镜头到引擎

**上游入口**：手上只有专题、没有镜头表时，先跑 `scripts/pick_cards.py --topic "<专题>"` 出六位骨架与候选卡，再把 `--json` 产物喂给本文件的路由表。

## 1. 镜头标签

每个镜头打四个标签，写成 JSON（`scripts/route.py` 的输入格式）：

| 字段 | 取值 | 怎么判断 |
|---|---|---|
| `dur` | 秒 | 这段画面自己讲完一件事的时间 |
| `kind` | `ui` / `data` / `scene` / `mixed` | 内容主体是卡片文字、还是数值图形、还是画面/光效 |
| `motion` | `cut` / `grow` / `loop` / `follow` | 跳切蒙太奇 / 一笔画出来、连续生长 / 循环背景 / 镜头跟着运动体走 |
| `text_heavy` | true / false | 该镜头里字数占比是否过半 |
| `layout_precise` | true / false | 是否需要像素级对齐参考片（复刻类任务几乎总是 true） |

## 2. 判定顺序

先命中先定，不要综合打分（打分会被次要维度带偏）：

```
motion==follow                                  → hyperframes（连续运镜，卡库没有跟拍卡）
kind==data 且 motion in (grow, loop)            → iart（draw(t) 本身就是连续生长）
grow 且 dur>6 且 kind in (ui, mixed)             → hyperframes（长镜头版式推移）
cut 且 kind==ui                                 → shotcraft
kind==scene 且 dur>6                            → hyperframes
motion==loop                                    → hyperframes
其他                                            → shotcraft（兜底）
```

**只有三个引擎，没有"自写组件"这条路。** 卡库对不上构图时的处理顺序是固定的：

1. 在 124 张里换一张同族、构图最接近的卡（榜单→榜单卡、对比→天平/双栏卡）；
2. 只改卡内文案、配色、数字与图片，不改卡的既有时序与版式；
3. 整页版式都套不上（原创排版、连续运镜、循环背景），才交给 hyperframes 重排整页 HTML。

`layout_precise` 不改变引擎判定，它只决定第 2 步的工作量：为 true 时按参考片的坐标微调卡内元素间距与字号，不改卡本身的动画。

## 3. 混合编排怎么落地

不要"三个引擎各渲一段再 ffmpeg 拼"。拼接会带来三处不一致，很难藏：

1. **色差**：iart/hyperframes 走浏览器 sRGB，Remotion 走另一条色彩链，接缝处会出现色调跳变
2. **字体渲染**：headless Chrome 与 Remotion 的 subpixel 抗锯齿不同，字幕粗细看起来不是一个人做的
3. **转场**：真拼接只能硬切或加叠化，做不了跨引擎的连续运镜

推荐做法：**统一到 Remotion 工程里做时间轴**，把 iart / hyperframes 的产物当"素材层"喂进去：

- iart：导出 300 帧 PNG 序列（`?t=n` 逐帧截图）→ Remotion `<Img>` 逐帧播放
- hyperframes：导出 PNG 序列或透明 MOV → 同上，可加 `opacity` 做淡入
- 只有在"片头完全独立、观众不会察觉接缝"时，才允许 ffmpeg concat

## 4. 能力矩阵（含可升级的官方 skill）

如果本机已装下列官方 skill，优先用它们替换对应层，本 skill 只保留路由与偏好：

| 层 | 本 skill 默认 | 更好的官方/维护版 | 装法 |
|---|---|---|---|
| 工程与渲染管线 | shotcraft 内置模板 | `remotion-dev/skills` 的 `remotion-create` / `remotion-render` / `remotion-best-practices`（官方，7.8K stars） | `npx skills add https://github.com/remotion-dev/skills --skill remotion-create` |
| 字幕 | 工程内 `<Sub>` 组件 | `remotion-captions`（官方，含逐词高亮） | 同上换 skill 名 |
| 长镜头 / 网页级动效 | hyperframes 直接调 | hyperframes 的意图层 `/hyperframes`（自带路由、Studio 预览、品牌 token） | `npx skills add https://github.com/heygen-com/hyperframes --skill hyperframes` |
| 数据可视化 | iart light tier | `iart-ai/motion-design-skills@remotion-video`、`iart-ai/manim-skills@manim`（数学/几何更强） | `npx skills add iart-ai/motion-design-skills --skill remotion-video` |
| 纯矢量动效（无代码） | — | `diffusionstudio/lottie@text-to-lottie`（文本直接出 Lottie） | 视需求 |

**注意**：hyperframes 的 `/hyperframes` 本身已经是一套"意图层 + 分发"，功能上与本 skill 的闸二重叠；它更完备但更重（带 Studio、品牌 token、更长的确认流程）。本 skill 的价值是**轻、中文优先、带实测坑与固定偏好**。两者同时可用时，重项目走 hyperframes 意图层，轻交付走本 skill。

### 升级项的实测结论（2026-11 实测，勿再重复试）

| 候选 | 实测 | 判定 |
|---|---|---|
| `remotion-render`（官方） | 照抄它的默认命令 → `concurrency is set higher than the amount of CPU cores available. Available CPU cores: 2, value set: 4`，11.5s 退出、0 帧。必须显式 `--concurrency` | **留，但命令要改写**；作为渲染参数参考 |
| `remotion-captions`（官方） | 依赖 `remotion elements use`，本项目 Remotion 4.0.484 无该子命令（只打印帮助）；转写需 whisper 模型；BasicCaptions 无中文描边 | **不接入**，字幕继续用工程内 `<Sub>` |
| `hyperframes` 意图层 | 未实跑（约 1.7M installs、86.5K stars），自带路由与 Studio | 重项目可试，**轻交付不用** |

## 5. 引擎实测成本（1080p / 90 帧 / 同机 / 2 核）

| 引擎 | 耗时 | 是否含编码 | 备注 |
|---|---|---|---|
| shotcraft / Remotion `--concurrency=2` | 33.7s | 是 | 最稳，默认选它 |
| hyperframes（自建 seek + 本地 GSAP） | 21.2s | 否 | 最快，但官方路径 0 帧 |
| iart（`?t=` 每帧重载） | 55.2s | 否 | 最慢，优势是可独立分发 |

**决策含义**：速度不构成选 iart 的理由；两者都能做时，一律留在 Remotion 工程里。

## 5. 什么时候不该进本 skill

- 用户要的是"视频美化/超分/换背景"→ 这是增强，不是渲染
- 用户明确要 AI 生成画面（Kling/Veo/Seedance）→ 不属 video-as-code
- 只是要一张封面图 → 走生图，不要开工程
