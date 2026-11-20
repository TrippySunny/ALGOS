# Задание 3. Топологическая сортировка и кратчайший путь

EDGES = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'E'),
    ('C', 'F'), ('D', 'G'), ('E', 'G'), ('E', 'H'), ('F', 'G'), ('G', 'H'),
]

def topo_sort(adj):
    state, order = {}, []
    def dfs(u):
        state[u] = 1
        for v in adj.get(u, []):
            if state.get(v) == 1:
                raise ValueError('Граф не является DAG!')
            if state.get(v) is None:
                dfs(v)
        state[u] = 2; order.append(u)
    for u in list(adj):
        if state.get(u) is None:
            dfs(u)
    return order[::-1]

def shortest_path(adj, s, t):
    from collections import deque
    prev = {s: None}
    q = deque([s])
    while q:
        u = q.popleft()
        if u == t: break
        for v in adj.get(u, []):
            if v not in prev:
                prev[v] = u; q.append(v)
    if t not in prev:
        return None, None
    path, u = [], t
    while u is not None:
        path.append(u); u = prev[u]
    return path[::-1], len(path) - 1

adj = {}
for u, v in EDGES:
    adj.setdefault(u, []).append(v)
    adj.setdefault(v, adj.get(v, []))  # вершина без исходящих

print('Топологический порядок:', topo_sort(adj))
path, length = shortest_path(adj, 'A', 'H')
print('Кратчайший путь A->H:', path, '| длина (рёбер):', length)
