# Задание 1. A* на взвешенном графе A→T

EDGES = [
    ('A', 'B', 3), ('A', 'C', 5), ('B', 'E', 1), ('B', 'D', 4),
    ('C', 'D', 2), ('C', 'F', 6), ('D', 'E', 3), ('D', 'G', 8),
    ('E', 'H', 5), ('F', 'G', 4), ('G', 'H', 2), ('G', 'T', 7), ('H', 'T', 6),
]
# Эвристика по условию: манхэттенское расстояние между координатами на рисунке
POS = {
    # 'A': (x, y), 'B': (x, y), ...
}
TX, TY = POS.get('T', (0, 0))

import heapq

def heuristic(v):
    x, y = POS.get(v, (0, 0))
    return (abs(x - TX) + abs(y - TY)) if POS else 0  # POS пуст -> h=0 (Дейкстра)

def astar(adj, s, t):
    # приоритетная очередь по f = g + h: g — точная стоимость от старта,
    # h — оценка до цели; вершина с min f исследуется первой
    openh = [(heuristic(s), 0, s)]
    g = {s: 0}; prev = {}; closed = set()
    while openh:
        _, gc, u = heapq.heappop(openh)
        if u in closed: continue
        closed.add(u)
        if u == t: break
        for v, w in adj.get(u, []):
            ng = gc + w   # новая стоимость пути до v через u
            if ng < g.get(v, float('inf')):
                g[v] = ng; prev[v] = u
                heapq.heappush(openh, (ng + heuristic(v), ng, v))
    path, u = [], t
    while u != s:
        path.append(u); u = prev[u]
    path.append(s)
    return path[::-1], g[t], closed

adj = {}
for u, v, w in EDGES:
    adj.setdefault(u, []).append((v, w))
    adj.setdefault(v, []).append((u, w))

path, cost, explored = astar(adj, 'A', 'T')
print('Путь A->T:', ' -> '.join(path))
print('Стоимость:', cost)
print('Исследовано вершин:', len(explored), sorted(explored))
