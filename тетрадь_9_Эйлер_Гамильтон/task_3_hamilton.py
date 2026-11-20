# Задание 3. Гамильтонов цикл

EDGES = [
    ('A', 'B'), ('A', 'C'), ('A', 'F'), ('B', 'D'), ('B', 'C'),
    ('C', 'D'), ('C', 'E'), ('D', 'F'), ('D', 'E'), ('E', 'F'),
]

from collections import defaultdict

def hamiltonian_cycle(adj):
    vs = list(adj); n = len(vs)
    def bt(path):
        if len(path) == n:
            return path if path[0] in adj[path[-1]] else None
        for v in adj[path[-1]]:
            if v not in path:
                r = bt(path + [v])
                if r: return r
        return None
    for s in vs:
        r = bt([s])
        if r: return r + [r[0]]
    return None

adj = defaultdict(set)
for u, v in EDGES:
    adj[u].add(v); adj[v].add(u)

# Теорема Дирака: если deg(v) >= n/2 = 3 для всех v -> граф гамильтонов
deg = {v: len(ns) for v, ns in adj.items()}
print('Степени:', deg)
print('Условие Дирака (deg >= 3 для всех):', all(d >= 3 for d in deg.values()))

cyc = hamiltonian_cycle(adj)
print('Гамильтонов цикл:', ' -> '.join(cyc) if cyc else 'НЕ найден')
