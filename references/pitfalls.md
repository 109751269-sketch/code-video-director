# 踩坑清单（已实测）

环境基线：Linux / 2 核 / 内存上限 4096 MiB / Node 22 / ffmpeg 4.4.2 / Chrome 在 `/opt/browser/chrome` / puppeteer-core 在 `/opt/runtime/nodejs/node_modules/puppeteer-core`。**`/tmp` 每轮会被清空，工程必须放可存活目录**（如 `/home/user/work/`）。

## shotcraft（React + Remotion）

工程在仓库的 `template/` 子目录，根目录 `package.json` 只有测试依赖，别在那里装。

```bash
cd template
npm install                       # Remotion 4.0.484 / React 19.2.7，约 2–3 分钟
npx remotion render src/index.ts <CompositionId> out/xxx.mp4 --concurrency=1
```

- **必须显式写 `--concurrency`**：不加参数时 Remotion 自己算出 4，直接报 `concurrency is set higher than the amount of CPU cores available. Available CPU cores: 2, value set: 4` 并 rc=1（实测 11.5s 就失败，一帧没渲）。官方 `remotion-render` 的命令**在这台机器上默认不可用**。
- 实测同一段 150 帧（1080×1920）：`--concurrency=1` 46.7s / 峰值 1.43GB；`--concurrency=2` 40.1s / 峰值 1.51GB。2 比 1 快约 14%，多 80MB。
- 取值建议：≤300 帧用 2，整片 900 帧用 1（长片并发更容易触顶 4GB）。
- 新增镜头：在 `src/Root.tsx` 里 `registerRoot` 的 `<Composition>` 增加一条，`durationInFrames` = 时长 × fps，写完重启渲染即可。
- 1085 帧 1080p 约 15–25 分钟；900 帧竖屏约 8 分钟。
- 首帧白屏、后续正常 → 通常是 `useCurrentFrame()` 之外用了 `Date.now()` 或 CSS `animation`，Remotion 无法 seek。

## hyperframes（HTML + CSS + GSAP → headless Chrome）

两个已踩过的坑，都会表现成"渲染 0 帧"，不要以为是脚本写错：

1. **官方模板通过 CDN 引 GSAP，且编译产物不复制 `assets/` 目录** → `window.__timelines` 永远不注册 → 求帧时什么都没动。
   修法：把 GSAP 下载到本地用相对路径引，或干脆不用 timeline，改成"暴露一个 `seek(t)` 函数"，由截图脚本按帧调用。
   实测报错链：`PAGEERROR: gsap is not defined` → `typeof window.__frameAt === 'undefined'` → 一帧都截不到。补齐本地 GSAP 后立即恢复：
   `curl -sL https://unpkg.com/gsap@3.13.0/dist/gsap.min.js -o assets/gsap.min.js`
2. **4GB 内存下官方 render 会进入 low-memory 截图模式**，60 秒内 `framesCompleted` 恒为 0。
   修法：自建 seek 契约 + puppeteer 逐帧截图，再用 ffmpeg 合成：

```bash
# 每帧截一张，t = frame / fps
ffmpeg -y -framerate 30 -i frames/%05d.png -c:v libx264 -pix_fmt yuv420p -crf 18 out.mp4
```

- 渲染前先单独验证 `seek(0)`、`seek(1.5)` 两帧画面不同，再批量跑。
- 修好后速度反而是三者最快：90 帧 1080p **21.2s**（不含编码）。

## iart（light tier：单 HTML + Canvas `draw(t)`）

- **不带 `?t=` 打开会启动 `requestAnimationFrame` 自播放**，用脚本手动求帧时会被 rAF 覆盖 → 截出来全是第 0 帧或随机帧。
  修法：URL 必须带 `?t=<秒>`，且页面在检测到该参数时不要启动 rAF。
- **`?t=` 是"每帧重新加载页面"，代价很高**：90 帧 1080p 实测 55.2s（0.61s/帧），比 Remotion 的 33.7s 还慢。要提速得改成 `window.__frameAt(t)` 页内 seek，别再重载。
- 它的真实优势是"可独立分发的单个 HTML"，不是速度。

## 通用

- 参考片先量再画：`ffprobe -v error -show_entries stream=width,height,r_frame_rate,nb_frames`。
- 手机录屏里的原片往往不是标准比例（我这支实测约 1.37:1，接近 4:3），**先裁内容区再量**，别按抖音默认竖屏套。
- 出片后必抽帧核对：`ffmpeg -ss <t> -i x.mp4 -frames:v 1 -q:v 2 chk.png`。
- ffmpeg 4.4.2 的 `hstack` 要求两路同高，拼对比图先统一 `scale=-2:720`。
- 渲染中断留下的半成品 mp4 能播放但时长异常，`ffprobe` 的 `nb_frames` 会明显小于预期 —— 交付前必须核。

## 字幕（remotion-captions 判定）

- 官方 `remotion-captions` 的显示路径依赖 `npx remotion elements use ...`，**本项目 Remotion 4.0.484 没有 `elements` 子命令**：执行后只打印 CLI 帮助，不写文件、不装包。
- 转写路径依赖 whisper（需下模型），而当前片子没有音轨，用不上。
- 中文硬字幕需要白描边（`WebkitTextStroke`），官方 BasicCaptions 不提供该样式。
- 结论：字幕继续用工程内 `<Sub>`，不并行引入第二套。真要做真人配音片且升级 Remotion 后，再单独评估。

## 渲染前预检（三条硬规则）

1. **数字只从 `src/data/*.json` 来**：柱状、字幕、榜单共用同一份数据，禁止在 JSX 写字面量。验收时抽一帧，把屏幕上的数与 JSON 对一遍。
2. **规格写进 `SPEC.md`**：画幅/fps/总帧数/composition id/输出路径/数据源，六行。所有命令从它取值。hyperframes 的默认时长是 **30 帧（1 秒）**，必须显式给时长，否则片头 1 秒就断。
3. **渲染前先出 3 帧**：`bash scripts/preflight.sh src/index.ts <Comp> 0 470 801`。空帧判定用亮度极差（<12 视为纯色），比"渲完再看"便宜两个数量级。
   - `npx remotion still` **同样受并发默认值影响**，实测不加 `--concurrency=1` 会直接报 `Maximum for --concurrency is 2`，一帧都不出。
