# 卡片索引（124 张 · 选卡用）

用途：给一个专题，先按题材关键词排序候选，再按"位"（hook/define/evidence/compare/verdict/outro）定卡。
数据源 `cards-index.json` 由 shotcraft 的 `gallery/api/library.json` 生成，`scripts/pick_cards.py` 直接读它。

| 卡名 | 类别 | 时长 | 能量 | 版式 | 适合位 | 一句话 |
|---|---|---|---|---|---|---|
| `brand-ink-open` | 开场与品牌 | 2.8g | low | 整屏标题 + 背景 | hook/define | 墨线十字准星描画→字标逐字压印→打字机副标→满一秒静止再上浮消散 |
| `crane-rise-reveal` | 开场与品牌 | 5.5g | high | 整屏标题 + 背景 | hook/define | 升降臂拉升揭示——开场怼在一行数据特写，相机沿 Y 轴减速升起后拉，行行涌入直到整面 dashboard 铺 |
| `dataviz-landscape-open` | 开场与品牌 | 8.0g | low | 整屏标题 + 背景 | evidence/hook/define | 暗场支流线束地景开场——多条流线汇入主干、虚构 ID 标签浮在线上、相机重景深低速飞越 |
| `fracture` | 开场与品牌 | 5.2g | high | 整屏标题 + 背景 | hook/define | 5×5 瓦片从 3D 碎片态按中心波纹逐圈聚合成整面海报，停一拍亮字，随后全部碎片背离中心加速旋转飞出画面 |
| `icon-field-colorize` | 开场与品牌 | 6.0g | mid | 整屏标题 + 背景 | hook/define | 灰阶小图标点阵错峰浮现铺满全屏，停一拍后多道品牌色横带波纹极快向下扫翻全场——"功能全景先摆满，品牌一瞬间点 |
| `letterspace-materialize` | 开场与品牌 | 4.0g | low | 整屏标题 + 背景 | hook/define | 大字距字标全字符并行连续描画结晶——所有字母同帧起笔、笔画像手写一样连续生长、同帧齐收成词；氛围底景上的品牌 |
| `magician-card-flourish` | 开场与品牌 | 0.3g | high | 整屏标题 + 背景 | hook/define | 午夜蓝暗场上蓝色星芒闪现 0.3s（X 形针状光束旋转 90°+中心辉光放射小光芒），卡片从闪光点弹射而出— |
| `orbit-ring-title-open` | 开场与品牌 | 5.0g | mid | 整屏标题 + 背景 | hook/define | 石墨暗场上八张 16:9 暗色内容卡按 45° 均布在 720×380 椭圆上匀速公转（卡身永不倾斜，纵深只 |
| `spotlight-hero-card` | 开场与品牌 | 5.7g | high | 整屏标题 + 背景 | hook/define | 关灯的剧场里一束钨丝聚光（带体积光柱）扫过页面锁定一张卡，斜侧推进后卡片弹起悬浮、香槟色光束沿轮廓两圈、连同 |
| `stroke-segment-build` | 开场与品牌 | 5.5g | low | 整屏标题 + 背景 | hook/define | 断笔成字——标题拆成十几段互不相连的笔画乱序逐段点亮，前 70% 不可读，末段落位瞬间语义"啪"地成立 |
| `text-as-mask` | 开场与品牌 | 5.5g | high | 整屏标题 + 背景 | hook/define | 文字视频遮罩——瓷白舞台上切出超粗大标题字，字内部透出缓慢平移的暗色实时产品面板，结尾吸一口气后字形指数冲入 |
| `blur-slide` | 字体与排版 | 4.0g | low | 全屏字 / 版式 | hook/verdict | 标题逐词入场，y 0.38em→0 + blur 18→0 + opacity 0→1 三通道走同一条 ea |
| `brace-expand` | 字体与排版 | 4.0g | mid | 全屏字 / 版式 | hook/verdict | 一对紧贴的小花括号先在正中出现，随即带一次过冲向左右弹开并放大到标题级，文字 clip 宽度严格绑括号内缘、 |
| `countdown-arc-scatter` | 字体与排版 | 3.3g | high | 全屏字 / 版式 | hook/verdict | 纸面表盘 9 个等大数字沿大弧切向排布，整盘扫过 96° 后减速急停，"5" 停在弧顶随即平移落位成标题首字 |
| `document-typewriter-reveal` | 字体与排版 | 5.0g | low | 全屏字 / 版式 | hook/verdict | 悬浮在暗场里的整页真排版文档窗口在光标后自己"写"出来、侧栏跟进、历史条目逐个落入轨道，相机从斜侧标题特写一 |
| `flying-words` | 字体与排版 | 6.0g | high | 全屏字 / 版式 | hook/verdict | 22 个关键词按黄金角铺在扁椭圆截面上，沿 z 轴从远处飞到相机前擦身而过，透明度走 [0,1,0.5,0. |
| `glitch-cycle` | 字体与排版 | 5.6g | high | 全屏字 / 版式 | hook/verdict | 同一行等宽槽位循环轮播 4 条状态短语，每条头尾按概率关键帧 [1,0,0,0.1,0,0,1] 全乱码、中 |
| `gradient-word-sweep` | 字体与排版 | 2.0g | high | 全屏字 / 版式 | hook/verdict | 黑底标语里关键词被渐变彩光从左到右快速扫过"充能"——波前字符辉光最强向后衰减，填满后字符间勾连细紫红闪电、 |
| `lead-word-zoom-assemble` | 字体与排版 | 2.8g | high | 全屏字 / 版式 | hook/verdict | 首词以 2.3 倍字号占据画面中央、hold 期间继续推近 6%，随后一条曲线同时完成「缩回终字号」与「整行 |
| `marker-underline-title` | 字体与排版 | 1.5g | low | 全屏字 / 版式 | hook/verdict | 大标题落定后，关键词下方马克笔下划线从左到右快速描画——变宽笔形、毛糙边缘、微上斜跟随斜体字势，贴着字底 |
| `outline-word-fill` | 字体与排版 | 3.0g | high | 全屏字 / 版式 | hook/verdict | 空心词（细暖灰描边、500 字重）从 3.2 倍急缓收缩落位，虚线大圆随后从 2.8 倍收到字周围并缓慢自转 |
| `paper-title-card` | 字体与排版 | 1.8g | low | 全屏字 / 版式 | hook/verdict | 一句话逐词压印上纸、一个词标强调色斜体、短划线收束 |
| `pill-chip-slot-cycle-handled` | 字体与排版 | 5.0g | mid | 全屏字 / 版式 | hook/verdict | 白底句式 "Your `chip` Handled" 里深色胶囊内词竖向滚轮轮换，胶囊宽度按预量文本宽插值平 |
| `pill-slot-cycle` | 字体与排版 | 6.7g | mid | 全屏字 / 版式 | hook/verdict | 句中词槽轮换——固定句干钉死不动，句尾 pill 徽章每 ~0.7s 老虎机滚一格（旧的上飞加速淡出、新的从 |
| `text-column-converge` | 字体与排版 | 6.0g | low | 全屏字 / 版式 | hook/verdict | 双词对峙合拢——左"NEW"右特性词钉死在等屏边距两侧硬切轮换、全程零收缩，换到最后一词才唯一一次 ease |
| `title-demote-to-label` | 字体与排版 | 3.7g | low | 全屏字 / 版式 | hook/verdict | 大标题降格为节标签两式——A 大标题居中显影站稳一拍后连续缩小 0.3x 平移到左上角落成小节标签、内容区在 |
| `type-assembly-moves` | 字体与排版 | 5.5g | mixed | 全屏字 / 版式 | hook/verdict | 文字集结三式——split-text-stagger 逐字裂升、letterform-drift-assem |
| `type-entrance-moves` | 字体与排版 | 5.0g | high | 全屏字 / 版式 | hook/verdict | 标题文字入场一式——letter-drop-physics 字符坠落（重力砸落、弹跳、歪斜站定，最后一拍集体 |
| `type-rhythm-sync` | 字体与排版 | 5.5g | mixed | 全屏字 / 版式 | hook/verdict | 文字随声同步两式——font-weight-pump 字重脉冲（笔画随鼓点变粗弹回）与 karaoke-fi |
| `typewriter-moves` | 字体与排版 | 5.3g | low | 全屏字 / 版式 | hook/verdict | 打字机 error-retype——误删重打的"改口"三幕剧：打出平庸词 → 犹豫 → 退格删掉 → 更快打 |
| `vertical-word-roll-blur-cycle` | 字体与排版 | 5.0g | mid | 全屏字 / 版式 | hook/verdict | 句尾词换成竖向滚轮，3 次换词各 0.55s（outQuint 七成 + outBack 三成，前快后极慢带 |
| `word-relay-filmstrip` | 字体与排版 | 2.0g | low | 全屏字 / 版式 | hook/verdict | 左列黑白相间等高页面卡步进滚动（焦点卡全亮、邻卡离焦压暗）、右侧衬线大词原位接力（名词恒定+动词轮换）——切 |
| `word-relay-geometry` | 字体与排版 | 6.0g | high | 全屏字 / 版式 | hook/verdict | 三个利益词各带一套专属几何接力——虚线大圆减速自转 + 彗星弧飞跑 → 三实线圆 trim 依次生长后收拢咬 |
| `assemble-then-type-flyin` | 特效与光 | 5.6g | high | 全屏光效 / 材质 | hook/define/evidence | 空的暗底网格上，无文字的组件骨架先从四面八方飞入贴合；随后各处文字逐字从 3D 空间旋转着飞来落位，先大标题 |
| `aurora-bloom-bg-flip` | 特效与光 | 5.2g | ramp | 全屏光效 / 材质 | define/evidence | 浅灰底从底部升起紫橙柔焦 blob，随后整个底色在约 0.36s 内压暗到近黑、blob 压成余晖；文案同步 |
| `brand-frame-snap` | 特效与光 | 4.7g | mid | 全屏光效 / 材质 | define/evidence | 品牌色画框语法——一圈粗纯色画框先于内容长出包住全屏，录屏窗口落进框内；模式切换时整圈画框同帧硬翻色+窗内布 |
| `fui-hud-moves` | 特效与光 | 3.0g | high | 全屏光效 / 材质 | define/evidence | FUI/HUD 准星咬合——reticle-lock-on 四个 L 形角标组成的取景框从画外飞入、超调回弹 |
| `glow-flyline-moves` | 特效与光 | 5.7g | mixed | 全屏光效 / 材质 | define/evidence | 暗场光斑与飞线三式——glow-orb-ambient 光斑底噪、flyline-arc 飞线连接、orb- |
| `icon-performance-moves` | 特效与光 | 5.2g | mid | 全屏光效 / 材质 | define/evidence | 图标表演——attention-bounce 求关注弹跳（图标连跳递增+落地压扁+镜头被吸引） |
| `impact-feedback` | 特效与光 | 5.0g | high | 全屏光效 / 材质 | define/evidence | 命中反馈两式——hit-counter 连招计数（顿帧+伤害数字+combo 跳字）、anime-impac |
| `light-play-moves` | 特效与光 | 5.7g | mixed | 全屏光效 / 材质 | define/evidence | 光效两式——spotlight-sweep 聚光扫字、sheen 单点扫光 |
| `radial-ripple-phone-chips` | 特效与光 | 5.6g | low | 全屏光效 / 材质 | define/evidence | 暖沙底四层同心圆错相呼吸如水波，中央手机 mockup 屏内 feed 自动缓滚，两侧白色 chip 先后  |
| `riso-print-hits` | 特效与光 | 4.0g | high | 全屏光效 / 材质 | define/evidence | 套印错位冲击帧——riso-misregistration-hit 单发：标题撞停瞬间裂成双色 riso 印 |
| `scan-bracket-sweep` | 特效与光 | 5.0g | low | 全屏光效 / 材质 | define/evidence | 文档弹到中央，四角落下 L 形取景括号，一条扫描光带拖着渐变尾迹在文档上往复扫 5 趟——文档全程静止，只有 |
| `scanline-annotate-focus` | 特效与光 | 5.0g | mid | 全屏光效 / 材质 | define/evidence | 一条扫描线自上而下匀速掠过已存在的页面，越过哪块区块的下缘，哪块就被四角取景框从外扩处弹簧收拢对准（一次过冲 |
| `scanline-assemble-flyin` | 特效与光 | 5.2g | high | 全屏光效 / 材质 | define/evidence | 页面开场是一张只有网格与虚线槽位的蓝图画板，一条亮扫描线自上而下掠过；扫到每个槽位，该处组件就从画外飞入过冲 |
| `slam-entrance-moves` | 特效与光 | 0.7g | high | 全屏光效 / 材质 | hook/define/evidence | 高能砸入三式——kanada-perspective-snap 金田透视急停、score-slam 比分砸落 |
| `spotlight-sweep-moves` | 特效与光 | 4.5g | low | 全屏光效 / 材质 | define/evidence | 暗场聚光显影三式——A 醒睡扫过（光到即亮光走即暗）、B 贴边泛光横摇（紫光贴 UI 边缘渗入+聚光匀速右移 |
| `before-after-slider-scrub` | 数据可视化 | 5.0g | mid | 图表满版 | evidence | 前后对比拉杆——"处理前/后"两版叠放，分割杆先猛甩后慢扫，杆过处新版"显影"揭出 |
| `chart-live-moves` | 数据可视化 | 6.4g | high | 图表满版 | evidence | 活体图表三式——oscilloscope-stream 示波流线（曲线右端实时写入+突发尖峰）、unit-d |
| `gauge-readout-moves` | 数据可视化 | 4.7g | high | 图表满版 | evidence | 仪表读数两式——needle-sweep-selftest 满弧扫针（点火自检指针甩满全弧再回落真值）与 t |
| `scroll-brake-moves` | 数据可视化 | 5.0g | high | 图表满版 | evidence | 长卷急刹两式——changelog-scroll-brake 基本款（高速长卷指数减速精准停位+目标抬升）与 |
| `timeline-travel` | 数据可视化 | 5.0g | high | 图表满版 | evidence | 时间轴横移——镜头沿水平刻度轴加速掠过版本刻度，每过一格卡片弹立短停，末刻度急停推近 |
| `avatar-bracket-carousel` | UI 入场 | 5.2g | mid | 卡片簇 / 整页 | compare/evidence | "Your ___ agent" 填空排版，四角对焦框钉在句中不动，头像队列在框内垂直 spring 轮换三 |
| `bezier-source-converge-merge` | UI 入场 | 5.6g | mid | 卡片簇 / 整页 | compare/evidence | 左侧四个来源节点各有一条细贝塞尔曲线连向右侧同一汇聚点，曲线先错峰由左向右 draw-on，节点沿自己的曲线 |
| `card-stack` | UI 入场 | 5.0g | high | 卡片簇 / 整页 | compare/evidence | 一组模板卡（demo 9 张）从屏幕下方逐张 spring 弹入、越落越快叠成一摞，全员落位后整摞一次性展成 |
| `carousel-3d` | UI 入场 | 5.6g | mid | 卡片簇 / 整页 | compare/evidence | 8 张卡排成圆环整环自转一圈（匀速底 + 每 45° 一次停靠的分步），每卡只绕 Y 公转、自身 billb |
| `cloner-depth-echo` | UI 入场 | 4.6g | mid | 卡片簇 / 整页 | compare/evidence | 克隆纵队——主卡瞬间"复印"出 7 个半透明分身沿斜向纵深排开成队，停一拍后全体加速吸回本体合一+弹跳 |
| `deck-deal-flyin` | UI 入场 | 5.0g | high | 卡片簇 / 整页 | compare/evidence | 暗色石墨桌面上的实体牌堆特写环绕开局，灯从牌堆亮到旁边的页面板，一摞卡像发牌一样硬加速甩进网格，相机追着发牌 |
| `doc-park-left-pill-deal` | UI 入场 | 5.8g | low | 卡片簇 / 整页 | compare/evidence | 文档不淡出而是向左滑出只露约 35% 宽并微缩到 0.92，右侧按旁白节奏慢速发牌三张白底描边药丸（outB |
| `draw-svg-trace` | UI 入场 | 4.4g | mid | 卡片簇 / 整页 | compare/evidence | 描边生长圈注——一条带笔头的墨线沿元素轮廓跑一圈把它"画"出来，闭合瞬间闪黑交棒、内容淡入；同套路可给标题画 |
| `element-body-moves` | UI 入场 | 5.0g | mixed | 卡片簇 / 整页 | compare/evidence | 元素身体感——contact-shadow-lift 接触阴影离面抬升：卡抬起时桌上的阴影同步放大变淡，纸片 |
| `integration-hub-map` | UI 入场 | 0.5g | high | 卡片簇 / 整页 | compare/evidence | 旧页面一次性快翻 180°（侧棱瞬间亮闪）落成新中枢页，五个集成 app 图标同帧弹现、随即五条彩虹光管同帧 |
| `list-reveal` | UI 入场 | 4.0g | low | 卡片簇 / 整页 | compare/evidence | 垂直菜单 6 项按 10f 的间隔依次 scale 找位、软 back 轻微过冲落定，同时整个列表容器全程匀 |
| `list-stack-press` | UI 入场 | 3.0g | mid | 卡片簇 / 整页 | compare/evidence | 列表卡从画面底部逐张飞上摞起，每张落地压弹整摞、计数器同步跳一格 |
| `neon-frame-forerun` | UI 入场 | 0.7g | high | 卡片簇 / 整页 | compare/evidence | 强透视直角霓虹框自左缘两头奔画先行成型，页面在框内由暗转亮，同时框内组件/文字从 3D 上空带同形软影错峰贴 |
| `neon-frame-orbit-drop` | UI 入场 | 0.5g | high | 卡片簇 / 整页 | compare/evidence | 霓虹框先行描框后，镜头绕页面左→右弧线旋转，页面全部组件/文字**同帧**从空中往下贴合（同形软影同步收敛） |
| `page-waterfall-wall` | UI 入场 | 6.0g | mid | 卡片簇 / 整页 | compare/evidence | 页面瀑布墙——真实页面截图切成 3–4 列在 3D 后仰墙面上差速反向无限滚动，视差 + 镜头缓推做"内容多 |
| `product-card-progressive-assemble` | UI 入场 | 5.7g | mid | 卡片簇 / 整页 | compare/evidence | 详情卡像被逐字段抓取般自建——一枚"填充光标"领先跳格，图→标题→分类 pill 依次 pop→原价出现后被 |
| `radial-wave` | UI 入场 | 3.8g | high | 卡片簇 / 整页 | compare/evidence | 17×9 圆点阵列按到波源的欧氏距离错峰点亮，每点 scale 过冲到 1.5 再落回常亮，第一道波扫完后第 |
| `research-card-stack-scroll` | UI 入场 | 4.8g | high | 卡片簇 / 整页 | compare/evidence | 深色论文卡每 12 帧一张沿右下轴线飞入中心叠压，落位带 1 帧压缩，只有最上一张全清晰渲染标题+作者+摘要 |
| `row-embed` | UI 入场 | 2.0g | mid | 卡片簇 / 整页 | compare/evidence | 内容行像卡片一样从空中降下、rotateX 收平、嵌入瞬间底边亮一道强调色的缝 |
| `value-stagger-gradient` | UI 入场 | 5.0g | high | 卡片簇 / 整页 | compare/evidence | 16 根柱入场时 delay 是时间错峰，同时高度/色相/位移/模糊四个属性各自铺成从首到末的数值梯度；第二 |
| `wall-reveal-moves` | UI 入场 | 5.0g | mid | 卡片簇 / 整页 | compare/evidence | 整墙批量入场两式——bento 逐格点亮、蓝图描线成形，全部原位显形不位移，与 deck-deal-flyi |
| `autolayout-gap-dial` | 交互演示 | 5.0g | mid | 界面操作特写 | evidence/compare | 间距拨盘驱动布局——一排链接块带框选描边+缝隙间距标注，徽章数字逐格跳动、块被参数实时推开再弹簧回弹归位；" |
| `canvas-materialize-moves` | 交互演示 | 5.0g | mid | 界面操作特写 | evidence/compare | 内容"物化上画布"两式——panel-to-canvas 行倒卡（面板表格行沿弧线飞出、跨容器变形成画布卡片 |
| `chip-grid-single-select-blackout` | 交互演示 | 5.5g | low | 界面操作特写 | evidence/compare | 五个选项 chip 以 3+2 居中排布逐个淡入；选中帧先插一帧灰色按压块，紧接数帧内底色变墨黑、文字变白并 |
| `collab-cursor-moves` | 交互演示 | 5.2g | mixed | 界面操作特写 | evidence/compare | 协作光标当演员——cast-ensemble 五光标群演氛围层（错峰飞入+正弦漂移+打字 cameo+聚拢围 |
| `glass-pill-dictation-typing` | 交互演示 | 3.3g | low | 界面操作特写 | evidence/compare | 一条定宽玻璃胶囊以约 1.25 倍略大弹出后缓落到位，内部自左淡到右浓铺一层强调色暖光；光标先行、随后匀速打 |
| `hashtag-to-pill-materialize` | 交互演示 | 4.0g | mid | 界面操作特写 | evidence/compare | 话题词打字实体化——居中打出 "#word"（红实心光标恒亮），1 帧硬切变成宽大胶囊标签，hold 后缩小 |
| `picker-carousel-feature-cycle` | 交互演示 | 3.6g | mid | 界面操作特写 | evidence/compare | 移动端风竖向选择器——焦点药丸不动、内容穿过它，每项带明显 outQuint 减速吸附后完全静止，按到中心距 |
| `segmented-thumb-hero` | 交互演示 | 3.5g | mid | 界面操作特写 | evidence/compare | 分段控件 thumb 位移当主角特写——超大胶囊 segmented control 弹簧浮入，描边箭头光标 |
| `theme-switch-moves` | 交互演示 | 4.7g | mixed | 界面操作特写 | evidence/compare | 主题切换两式——theme-sweep 斜向扫场（边界扫过处就地换肤）与 palette-ripple 组合 |
| `type-and-filter` | 交互演示 | 2.5g | high | 界面操作特写 | hook/evidence/compare | 真实 UI 上打字搜索、网格自己收敛成一张卡、点击穿透进详情页 |
| `voice-waveform-live` | 交互演示 | 5.7g | mid | 界面操作特写 | evidence/compare | 录音胶囊实时声纹——64 根细竖条随"说话"起伏，说话时中部高耸、停顿缩成点线，波形从右往左滚动；说→停→说 |
| `basic-3d-scene` | 摄影机运动 | 7.5g | mid | 空间 / 透视 | hook/evidence | impress.js 式空间演示：卡片以不同位置/旋转/缩放散布 3D 空间，相机取各步姿态之逆依次飞行对齐 |
| `crash-zoom-punch` | 摄影机运动 | 0.5g | high | 空间 / 透视 | hook/evidence | 全景一拍急推到目标特写（6f），落位二选一——过冲回弹（弹性）或撞停震屏（重量） |
| `cursor-flyover` | 摄影机运动 | 8.0g | mid | 空间 / 透视 | hook/evidence | 整页俯瞰后，相机依次飞到四个功能区 zoom-in 特写，SVG 光标先一步到位指点、点击留下涟漪并触发界面 |
| `depth-layer-moves` | 摄影机运动 | 5.5g | mid | 空间 / 透视 | hook/evidence | 分层深度运镜——多层视差滑轨：3 层速度梯度横移出纵深，滑轨落定时主角浮起 |
| `graze-face-tour` | 摄影机运动 | 5.0g | high | 空间 / 透视 | hook/evidence | 大倾角贴面游走特写——镜头贴着 UI 表面低飞掠过（侧栏树/顶栏/列表当地形），页面文字初始悬浮在界面上空带 |
| `overhead-camera-moves` | 摄影机运动 | 4.0g | mixed | 空间 / 透视 | hook/evidence | 俯拍揭示两式——tilt-reveal 俯仰抬正揭示、overhead-tabletop-drop 桌面卡阵 |
| `space-camera-moves` | 摄影机运动 | 5.7g | high | 空间 / 透视 | hook/evidence | 3D 空间化运镜两式——exploded-view 爆炸分解（构件沿 Z 炸开再合体）、drone-dive |
| `steep-tilt-glide` | 摄影机运动 | 4.0g | high | 空间 / 透视 | hook/evidence | 固定镜头下直立页面以 60° 强透视侧立（右近左远），页面自身沿其 3D 横面方向滑移掠过镜头（物动镜不动） |
| `tension-camera-moves` | 摄影机运动 | 6.0g | mixed | 空间 / 透视 | hook/evidence | 情绪运镜两式——bullet-time 冻结环绕、pull-back 拉远孤立，相机替观众"感受"而非"看" |
| `terminal-3d` | 摄影机运动 | 8.2g | mid | 空间 / 透视 | hook/evidence | 三个终端窗散布 3D 空间，相机窗间飞行、途中正弦拉远，每到一窗打字机敲命令、结果逐行滑出——命令执行的空间 |
| `beat-cut-moves` | 节奏剪辑 | 4.7g | high | 多格 / 快切 | compare/hook | 硬切当节拍乐器——连闪定格：三次白闪各硬切同一画面的一个裁切（全景→卡片→特写），快门余韵沉降后停在特写收束 |
| `beat-step-list-theme-cycle` | 节奏剪辑 | 4.7g | high | 多格 / 快切 | compare/hook | 三通道节拍器——深色场形容词列表逐拍上移一行，视口中央固定胶囊"接住"下一个词并换色，整场底色同拍跟换；行、 |
| `panel-grid-moves` | 节奏剪辑 | 5.2g | high | 多格 / 快切 | compare/hook | 分格节奏——comic-panel-split 漫画斜格劈出同一主体的三个机位，咔咔咔三格定格后末格斜边吃屏 |
| `quad-split-parallel-scenes` | 节奏剪辑 | 3.0g | high | 多格 / 快切 | compare/hook | 画面硬切 2×2 四宫格，四个象限并行跑各自的微场景（打字、急推、逐词、交互链），关键节拍错开 3–6 帧制 |
| `rhythm-interrupt-moves` | 节奏剪辑 | 4.5g | mixed | 多格 / 快切 | compare/hook | 打断节奏——jump-cut-punch-in 三级跳切推近：同构图三次无补间硬跳放大，逐级逼近目标 |
| `sakuga-timing-shift` | 节奏剪辑 | 5.0g | high | 多格 / 快切 | compare/hook | 一拍三转一拍一——元素先以每 3 帧一步的手翻书顿挫移动，高潮瞬间切成逐帧丝滑冲刺，帧率量化的突变本身就是看 |
| `speed-ramp-freeze` | 节奏剪辑 | 5.3g | high | 多格 / 快切 | compare/hook | 帧号非线性 remap 的节奏手法——定格标注（流动→定格圈注→解冻） |
| `trailer-grammar-moves` | 节奏剪辑 | 4.7g | mixed | 多格 / 快切 | compare/hook | 预告片语法一式——trailer-bumper 前置速剪钩子：三镜 9f 速剪 + 黑场静默一拍，再开场标题 |
| `bottom-push-stack-wipe` | 转场 | 5.7g | mid | 整屏过桥 | bridge | 底边上推换章——新场景连底色整屏从底边向上推入，把旧场景物理顶出画外，连推数章各配一种饱和底色，内容钉死在各 |
| `card-flip-reveal` | 转场 | 5.0g | high | 整屏过桥 | bridge | 功能卡 3D 翻面揭示——卡片沿 Y 轴翻 180°，正面 UI 翻到侧棱最薄处掠过一道随角度移动的受光，背 |
| `card-flock-tumble` | 转场 | 1.5g | high | 整屏过桥 | bridge | 三张 UI 页卡从侧棱薄边 3D 翻飞成阶梯站定（全程清晰、样条连续丝滑），站定后保持慢转不停，快速收束吸入 |
| `circle-match-iris` | 转场 | 5.5g | high | 整屏过桥 | bridge | 圆心匹配光圈切——光圈从页面上圆形元素的圆心炸开，圈内新页的圆形图表接在同一个圆上；匹配剪辑给光圈一个语义锚 |
| `gradient-transition` | 转场 | 6.7g | low | 整屏过桥 | bridge | 背景在 linear、radial、conic 三类 CSS 渐变间平滑过渡——角度、色标、中心、半径逐参数 |
| `line-carry-transition` | 转场 | 6.3g | mid | 整屏过桥 | bridge | 线条接力横移转场——场景 A 的进度条延伸出画，镜头跟线横移，线在移动中拐角围出场景 B 的卡框，全程无剪切 |
| `mosaic-reframe` | 转场 | 7.1g | mid | 整屏过桥 | bridge | 12 张瓦片在规则网格、feature mosaic、对角瀑布串三种排版间连续变形，位置宽高各自插值、逐片微 |
| `page-turn-transitions` | 转场 | 5.0g | high | 整屏过桥 | bridge | 整页体块转场——barn-door-split 对开门裂幕（旧页裂两半滑出、新页迎上） |
| `print-texture-transitions` | 转场 | 4.5g | mid | 整屏过桥 | hook/bridge | 印刷质感转场——ink-bleed-reveal 墨渗揭示（须状渗边洇开吃掉旧景） |
| `shot-transitions` | 转场 | 5.0g | mid | 整屏过桥 | bridge | 镜头交棒三式——推进流白、whip-pan 甩镜（急刹款）、mask-wipe 穿窗（纵深款），按能量落差与 |
| `tear-streak-transitions` | 转场 | 4.5g | high | 整屏过桥 | bridge | 撕裂转场——glitch-displace 噪声撕裂（16 横条错位抖动中硬切），数字故障语义的条带级撕裂 |
| `transition-hidden-cut` | 转场 | 5.0g | mid | 整屏过桥 | bridge | 藏切点转场三式——前景遮挡隐形切、对撞开屏、暖色漏光，硬切藏进遮挡/撞击/光峰的 1-3 帧里，观众看不见剪 |
| `transition-travel` | 转场 | 5.0g | mid | 整屏过桥 | bridge | 穿越式转场——字腔穿越：巨型章节标题的字形就是一扇窗，镜头钻进字形笔画完成换景 |
| `white-flash-logo-simplify-cut` | 转场 | 4.0g | high | 整屏过桥 | outro/bridge | 液态金属质感的彩色词标静置流光，蓄力后从字心炸出一记白闪过曝，曝光回落时同一位置已是扁平版字标——一次闪白完 |
| `wipe-transitions` | 转场 | 4.4g | mid | 整屏过桥 | bridge | 几何擦除转场——blinds-slice 百叶窗切条（12 根 3D 叶片错峰翻面成波，波扫过后整页由 A  |
| `grain-dissolve` | 收尾 | 2.0g | high | 标志 / 收尾 | outro | 整行字爆裂成沸腾颗粒噪点并浮现斜纹选区框，噪点云急速凝聚成更大号发光短字标，位移衰减归零定格 |
| `logo-shrink-wordmark-lockup` | 收尾 | 4.4g | mid | 标志 / 收尾 | hook/outro | 霓虹切口大环快速收束成中央实心小白 O、过冲刹车时换成 video-shotcraft 标志，图标左移让位， |
| `neon-triple-marquee` | 收尾 | 5.0g | high | 标志 / 收尾 | outro | 三行对向霓虹跑马灯 recap——三连词空心霓虹灯管巨字上中下排满一面斜拍的砖墙，奇偶行反向匀速无限横滚，三 |
| `outro-group-photo-launch` | 收尾 | 4.8g | mid | 标志 / 收尾 | outro | 全片元素从四面八方飞来围住字标合影，crane 落机位+舞台光+金尘做成发布会收场 |
| `ui-strip-away-outro` | 收尾 | 4.8g | mid | 标志 / 收尾 | outro | 减法式收尾——点击 Publish 后整个编辑器 UI 从外围到中心层层错峰蒸发，黑场上只剩那颗按钮滑到屏心 |
| `ui-to-brand-morph` | 收尾 | 4.3g | high | 标志 / 收尾 | outro | UI 变品牌两式——icon-flip-bloom 图标 Y 轴翻扁成竖线、从竖线撑开成品牌标志（琥珀斜切随 |
