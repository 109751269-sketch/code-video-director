#!/usr/bin/env python3
"""按专题从 124 张镜头卡里选候选卡（排序辅助，不是自动定稿）。

用法：
  python3 pick_cards.py --topic "AI 订阅套餐横评，ChatGPT/Claude/Gemini 价格与额度对比"
  python3 pick_cards.py --topic "..." --slot compare          # 只看某一位
  python3 pick_cards.py --topic "..." --json                  # 出 shots.json 骨架

输出：六个叙事位（hook/define/evidence/compare/verdict/outro）各三张候选 + 一句为什么。
最后一位需要人拍板——脚本只负责"有依据地排候选"，不负责审美判断。
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, '..', 'references', 'cards-index.json')

SLOTS = [
    ('hook', '钩子 0–4s', '先让人停下：一句话/一个数字的强开场'),
    ('define', '定义 4–9s', '一句话讲清这是什么东西'),
    ('evidence', '证据 9–17s', '拿数字、图表或操作画面作证'),
    ('compare', '对比 17–25s', '并列、排名、逐项判定'),
    ('verdict', '结论 25–31s', '大字落判，给出取舍'),
    ('outro', '收尾 31–36s', '标志定格 + 一句留白'),
]
AFFINITY = {
    'hook': {'opening': 4, 'rhythm': 3, 'typography': 2, 'camera': 2},
    'define': {'effects': 3, 'typography': 2, 'ui-entrance': 2, 'opening': 2},
    'evidence': {'data': 5, 'interaction': 3, 'ui-entrance': 2, 'effects': 1},
    'compare': {'ui-entrance': 4, 'rhythm': 3, 'data': 2, 'interaction': 1},
    'verdict': {'typography': 4, 'effects': 2, 'rhythm': 1},
    'outro': {'outro': 6, 'opening': 2},
}

ENERGY_FIT = {
    'hook': {'high': 3, 'mid': 1, 'ramp': 2, 'mixed': 2, 'low': -4},
    'define': {'mid': 3, 'low': 1, 'high': 0, 'ramp': 1, 'mixed': 1},
    'evidence': {'mid': 2, 'high': 2, 'ramp': 3, 'mixed': 2, 'low': 0},
    'compare': {'high': 3, 'mid': 1, 'ramp': 1, 'mixed': 2, 'low': -2},
    'verdict': {'high': 3, 'mid': 1, 'ramp': 2, 'mixed': 1, 'low': -1},
    'outro': {'low': 2, 'mid': 2, 'high': 1, 'ramp': 1, 'mixed': 1},
}

SYN = {
    '横评': ['榜单', '对比', '排名'], '测评': ['榜单', '对比', '评测'], '评测': ['榜单', '对比'],
    '对比': ['榜单', '并列'], '排行': ['榜单', '排名'], '榜单': ['排名', '并列'],
    '价格': ['数字', '对比'], '套餐': ['档位', '选择'], '订阅': ['档位', '付费'],
    '教程': ['讲解', '说明'], '科普': ['解释', '说明'], '发布': ['开场', '亮相'],
    '新品': ['亮相', '产品'], '年会': ['总结', '数据'], '复盘': ['数据', '结论'],
}

def tokens(topic):
    t = topic.lower()
    latin = {w for w in re.findall(r'[a-z0-9]{2,}', t)}
    cjk = re.findall(r'[\u4e00-\u9fff]+', topic)
    out = set(latin)
    for run in cjk:
        for n in (2, 3):
            for i in range(len(run) - n + 1):
                out.add(run[i:i + n])
    for t in list(out):
        out.update(SYN.get(t, []))
    # 去噪：常见虚词组合
    out -= {'的是', '这个', '一个', '我们', '可以', '什么', '如何', '以及', '进行', '因为', '所以'}
    return out

def score(card, toks, slot):
    s = 0.0
    name = card['name'].lower()
    blob_use = card['use']
    blob_sum = card['summary']
    for t in toks:
        if t in name:
            s += 6
        elif t in blob_use:
            s += 4
        elif t in blob_sum:
            s += 2.5
        elif t in card['catZh']:
            s += 2
    if card['slots'] and card['slots'][0] == slot:
        s += 8
    elif slot in card['slots']:
        s += 5
    s += ENERGY_FIT[slot].get(card['energy'], 0)
    s += AFFINITY[slot].get(card['cat'], 0)
    d = card['secs']
    if 3 <= d <= 7:
        s += 2
    elif d > 9 or d < 1.5:
        s -= 2
    return s

def pick(topic, per_slot=3):
    data = json.load(open(INDEX))
    cards = data['cards']
    toks = tokens(topic)
    out = []
    used = []
    taken = []
    for slot, label, hint in SLOTS:
        ranked = []
        for c in cards:
            if any(c['name'] == u for u in taken):
                continue
            sc = score(c, toks, slot)
            for u in used[-2:]:
                if u['cat'] == c['cat']:
                    sc -= 2.5
            ranked.append((sc, c))
        ranked.sort(key=lambda x: -x[0])
        top = [c for sc, c in ranked[:per_slot] if sc > 0] or [c for sc, c in ranked[:per_slot]]
        out.append({'slot': slot, 'label': label, 'hint': hint, 'candidates': top})
        used.append(top[0])
        for c in top:
            taken.append(c['name'])
    return toks, out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--topic', required=True)
    ap.add_argument('--slot')
    ap.add_argument('--per-slot', type=int, default=3)
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()

    toks, res = pick(a.topic, a.per_slot)
    if a.slot:
        res = [r for r in res if r['slot'] == a.slot]
    print('# 专题：%s' % a.topic)
    print('# 命中词：%s' % '、'.join(sorted(toks)[:14]))
    for r in res:
        print('\n## %s · %s   （%s）' % (r['slot'], r['label'], r['hint']))
        for i, c in enumerate(r['candidates'], 1):
            print('%d. `%s`  %s / %sg / %s / 首位 %s' % (
                i, c['name'], c['catZh'], c['secs'], c['energy'], '/'.join(c['slots'])))
            print('   %s' % c['use'][:90])
    if a.json:
        shots = []
        acc = 0
        for r in res:
            c = r['candidates'][0]
            dur = min(max(c['secs'], 2.5), 7.0)
            shots.append({'id': len(shots) + 1, 'start': round(acc, 1), 'dur': round(dur, 1),
                          'kind': kind_of(c), 'motion': motion_of(c), 'note': '%s · %s' % (c['name'], c['catZh']),
                          'card': c['name'], 'needs_review': True})
            acc += dur
        print('\n## shots.json 骨架（needs_review 全部为 true，改完再喂 route.py）')
        print(json.dumps({'title': a.topic[:20], 'canvas': '1920x1080', 'fps': 30, 'shots': shots},
                         ensure_ascii=False, indent=1))
    return 0

def kind_of(c):
    if c['cat'] == 'data':
        return 'data'
    if c['cat'] in ('camera', 'effects', 'opening', 'outro', 'transition'):
        return 'scene'
    return 'ui'

def motion_of(c):
    if c['cat'] == 'data':
        return 'grow'
    if c['cat'] == 'camera':
        return 'follow'
    if c['cat'] == 'transition':
        return 'cut'
    return 'cut'

if __name__ == '__main__':
    sys.exit(main())
