# Задание 3. Расписание занятий (граф конфликтов)

EDGES = [
    ('M1', 'M2'), ('M1', 'P1'), ('M1', 'M3'), ('M2', 'M3'),
    ('M2', 'P2'), ('M3', 'P1'), ('M3', 'P2'), ('M3', 'P3'),
    ('P1', 'P2'), ('P1', 'P3'), ('P2', 'P3'),
]

from collections import defaultdict

def welsh_powell(adj):
    deg = {v: len(ns) for v, ns in adj.items()}
    order = sorted(adj, key=lambda v: -deg[v])
    color = {}
    for v in order:
        used = {color[u] for u in adj[v] if u in color}
        c = 1
        while c in used: c += 1
        color[v] = c
    return color, order

adj = defaultdict(set)
for u, v in EDGES:
    adj[u].add(v); adj[v].add(u)

print('Степени:', {v: len(ns) for v, ns in adj.items()})
color, order = welsh_powell(adj)
slots = max(color.values())
print('Порядок:', order)
print('Раскраска (цвет = слот):', color)
print('Минимум временных слотов (χ):', slots)

sched = defaultdict(list)
for v, c in color.items():
    sched[c].append(v)
for c in sorted(sched):
    print(f'Слот {c}: {sched[c]}')

# проверка корректности
bad = [(u, v) for u, v in EDGES if color[u] == color[v]]
print('Конфликтов в одном слоте:', bad if bad else 'нет — OK')
