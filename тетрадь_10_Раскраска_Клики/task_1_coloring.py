# Задание 1. Раскраска графа

EDGES = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'),
    ('B', 'F'), ('C', 'D'), ('C', 'F'), ('C', 'G'), ('D', 'E'),
    ('D', 'G'), ('E', 'H'), ('F', 'G'), ('F', 'H'), ('G', 'H'),
]

from collections import defaultdict

def greedy_color(adj, order):
    color = {}
    for v in order:
        used = {color[u] for u in adj[v] if u in color}
        c = 1
        while c in used: c += 1
        color[v] = c
    return color

def welsh_powell(adj):
    deg = {v: len(ns) for v, ns in adj.items()}
    order = sorted(adj, key=lambda v: -deg[v])
    return order, greedy_color(adj, order)

def dsatur(adj):
    color = {}; sat = defaultdict(set)
    for _ in adj:
        # выбираем нераскрашенную вершину с max насыщенностью (при равенстве — степенью)
        v = max((x for x in adj if x not in color),
                key=lambda x: (len(sat[x]), len(adj[x])))
        used = {color[u] for u in adj[v] if u in color}
        c = 1
        while c in used: c += 1
        color[v] = c
        for u in adj[v]: sat[u].add(c)
    return color

adj = defaultdict(set)
for u, v in EDGES:
    adj[u].add(v); adj[v].add(u)

# простой жадный в произвольном порядке
order_wp, c_wp = welsh_powell(adj)
print('Степени:', {v: len(ns) for v, ns in adj.items()})
print('Порядок Вельша-Пауэлла:', order_wp)
print('WP раскраска:', c_wp, '-> цветов:', max(c_wp.values()))

c_ds = dsatur(adj)
print('DSatur раскраска:', c_ds, '-> цветов:', max(c_ds.values()))
