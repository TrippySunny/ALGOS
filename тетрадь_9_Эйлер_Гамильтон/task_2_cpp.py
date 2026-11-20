# Задание 2. Задача китайского почтальона

EDGES = [
    ('A', 'B', 6), ('A', 'D', 8), ('A', 'C', 3),
    ('B', 'D', 5), ('B', 'E', 4),
    ('C', 'D', 2), ('C', 'F', 7),
    ('D', 'E', 3), ('D', 'F', 6),
    ('E', 'F', 4), ('E', 'G', 5), ('F', 'G', 2),
]

from collections import defaultdict
import heapq

adj = defaultdict(dict)
for u, v, w in EDGES:
    adj[u][v] = w; adj[v][u] = w

# 1) вершины нечётной степени
deg = {v: len(ns) for v, ns in adj.items()}
odd = [v for v, d in deg.items() if d % 2 == 1]
print('Нечётные вершины:', odd, '| всего:', len(odd))

# 2) кратчайшие пути между всеми парами нечётных (Дейкстра из каждой)
def dijkstra(src):
    dist = {src: 0}; pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, 1e18): continue
        for v, w in adj[u].items():
            nd = d + w
            if nd < dist.get(v, 1e18):
                dist[v] = nd; heapq.heappush(pq, (nd, v))
    return dist

dists = {v: dijkstra(v) for v in odd}

# 3) минимальное паросочетание нечётных вершин: перебираем все способы
#    разбить их на пары и берём тот, где сумма кратчайших путей минимальна
#    (эти пути продублируем — все степени станут чётными)
def pairings(nodes):
    if not nodes:
        yield []
        return
    u = nodes[0]
    for i in range(1, len(nodes)):
        v = nodes[i]
        rest = nodes[1:i] + nodes[i + 1:]
        for pairs in pairings(rest):
            yield [(u, v)] + pairs

best_cost, best_pairs = float('inf'), None
for pairs in pairings(odd):
    c = sum(dists[u][v] for u, v in pairs)
    if c < best_cost:
        best_cost, best_pairs = c, pairs
print('Паросочетание:', best_pairs, '| добавленная длина:', best_cost)

# 4) итоговая длина маршрута почтальона
base = sum(w for _, _, w in EDGES)
print('Сумма рёбер графа:', base)
print('ИТОГО маршрут CPP:', base + best_cost)
