#!/usr/bin/env python3
"""从 shotcraft 卡库重新生成 references/cards-index.{json,md}。

卡库改动（新增/改名/改时长）后跑一次，索引才会跟上：
  python3 scripts/build_cards_index.py --library /path/to/shotcraft/gallery/api/library.json
不给 --library 时用默认 work 目录；库文件不存在就退出并提示，不会写半成品索引。
"""
import argparse, json, re, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_JSON = os.path.join(HERE, '..', 'references', 'cards-index.json')
OUT_MD = os.path.join(HERE, '..', 'references', 'cards-index.md')
DEFAULT_LIB = '/home/user/work/shotcraft/gallery/api/library.json'

CAT_ZH = {
    'opening': '开场与品牌', 'typography': '字体与排版', 'effects': '特效与光',
    'data': '数据可视化', 'ui-entrance': 'UI 入场', 'interaction': '交互演示',
    'camera': '摄影机运动', 'rhythm': '节奏剪辑', 'transition': '转场', 'outro': '收尾',
}
LAYOUT = {
    'opening': '整屏标题 + 背景', 'typography': '全屏字 / 版式', 'effects': '全屏光效 / 材质',
    'data': '图表满版', 'ui-entrance': '卡片簇 / 整页', 'interaction': '界面操作特写',
    'camera': '空间 / 透视', 'rhythm': '多格 / 快切', 'transition': '整屏过桥', 'outro': '标志 / 收尾',
}
BASE_SLOTS = {
    'opening': ['hook', 'define'], 'typography': ['hook', 'verdict'], 'effects': ['define', 'evidence'],
    'data': ['evidence'], 'ui-entrance': ['compare', 'evidence'], 'interaction': ['evidence', 'compare'],
    'camera': ['hook', 'evidence'], 'rhythm': ['compare', 'hook'], 'transition': ['bridge'],
    'outro': ['outro'],
}

def secs(dur):
    m = re.search(r'(\d+(?:\.\d+)?)s', dur)
    if m:
        return float(m.group(1))
    m = re.search(r'(\d+)f', dur)
    return round(int(m.group(1)) / 30, 1) if m else 5.0

def energy(e):
    if not e:
        return 'mid'
    head = e[:6]
    if '由低到高' in head:
        return 'ramp'
    if head.startswith('A '):
        return 'mixed'
    if '高' in head:
        return 'high'
    if '低' in head:
        return 'low'
    return 'mid'

def slots_for(cat, name):
    s = list(BASE_SLOTS[cat])
    n = name.lower()
    if any(k in n for k in ('split', 'versus', 'vs', 'compare', 'versus', 'quad', 'versus')):
        s = ['compare'] + [x for x in s if x != 'compare']
    if any(k in n for k in ('chart', 'gauge', 'timeline', 'dot', 'data', 'meter', 'axis', 'counter')):
        s = ['evidence'] + [x for x in s if x != 'evidence']
    if any(k in n for k in ('logo', 'outro', 'wordmark', 'lockup', 'marquee')):
        s = ['outro'] + [x for x in s if x != 'outro']
    if any(k in n for k in ('title', 'word', 'type', 'letter', 'text', 'headline', 'kinetic', 'slam')):
        s = ['hook'] + [x for x in s if x != 'hook']
    return s[:3]

ap = argparse.ArgumentParser()
ap.add_argument('--library', default=DEFAULT_LIB)
args = ap.parse_args()
SRC = args.library
if not os.path.exists(SRC):
    sys.exit(f'卡库不存在：{SRC}\n用 --library 指定 shotcraft/gallery/api/library.json 的真实路径')
d = json.load(open(SRC))
cards = []
for c in d['cards']:
    cards.append({
        'name': c['name'],
        'cat': c['category'],
        'catZh': CAT_ZH[c['category']],
        'layout': LAYOUT[c['category']],
        'secs': secs(c['duration']),
        'energy': energy(c.get('energy', '')),
        'slots': slots_for(c['category'], c['name']),
        'summary': re.sub(r'\s+', ' ', c['summary'])[:120],
        'use': re.sub(r'\s+', ' ', c['use'])[:120],
    })

order = list(CAT_ZH)
cards.sort(key=lambda x: (order.index(x['cat']), x['name']))
json.dump({'version': 1, 'source': 'video-shotcraft/gallery/api/library.json',
           'count': len(cards), 'cards': cards, 'slots': {
               'hook': '钩子 0–4s：先让人停下', 'define': '定义 4–10s：一句话讲清是什么',
               'evidence': '证据 10–18s：数字/图表/操作', 'compare': '对比 18–26s：并列与判定',
               'verdict': '结论 26–32s：大字落判', 'outro': '收尾 32–36s：标志定格',
               'bridge': '过桥：镜头之间的转场'}},
          open(OUT_JSON, 'w'), ensure_ascii=False, indent=1)

rows = ['# 卡片索引（124 张 · 选卡用）', '',
        '用途：给一个专题，先按题材关键词排序候选，再按"位"（hook/define/evidence/compare/verdict/outro）定卡。',
        '数据源 `cards-index.json` 由 shotcraft 的 `gallery/api/library.json` 生成，`scripts/pick_cards.py` 直接读它。', '',
        '| 卡名 | 类别 | 时长 | 能量 | 版式 | 适合位 | 一句话 |',
        '|---|---|---|---|---|---|---|']
for c in cards:
    rows.append('| `%s` | %s | %sg | %s | %s | %s | %s |' % (
        c['name'], c['catZh'], c['secs'], c['energy'], c['layout'],
        '/'.join(c['slots']), c['summary'][:54].replace('|', '/').replace('\n', ' ')))
open(OUT_MD, 'w').write('\n'.join(rows) + '\n')
print(len(cards), 'cards ->', OUT_JSON)
print('md lines', len(rows))
