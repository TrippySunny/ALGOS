# Задание 1. Обход графа DFS и BFS

EDGES = [
    (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7),
    (4, 8), (5, 8), (6, 9), (7, 9), (8, 10), (9, 10),
]
START = 1

def build_adj(edges, directed=False):
    adj = {}
    for u, v in edges:
        adj.setdefault(u, []).append(v)
        if not directed:
            adj.setdefault(v, []).append(u)
    return adj

def dfs(adj, start):
    # рекурсивный обход в глубину: идём к первому непосещённому соседу,
    # при тупике возвращаемся (backtracking)
    seen, order = set(), []
    def rec(u):
        seen.add(u); order.append(u)
        for v in adj.get(u, []):
            if v not in seen:
                rec(v)
    rec(start)
    return order

def bfs(adj, start):
    # обход в ширину: очередь, вершины посещаются «волнами» по расстоянию от старта
    from collections import deque
    seen, order = {start}, []
    q = deque([start])
    while q:
        u = q.popleft(); order.append(u)
        for v in adj.get(u, []):
            if v not in seen:
                seen.add(v); q.append(v)
    return order

adj = build_adj(EDGES)
print('Словарь смежности:', adj)
print('DFS порядок:', dfs(adj, START))
print('BFS порядок:', bfs(adj, START))
