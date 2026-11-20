# Задание 2. Компоненты связности и двудольность

EDGES = [
    ('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'),
    ('E', 'F'), ('F', 'G'),
    ('I', 'J'), ('I', 'L'), ('J', 'K'), ('L', 'K'),
    # H — изолированная вершина (без рёбер)
]

def build_adj(edges):
    adj = {}
    for u, v in edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    return adj

def components(adj):
    seen, comps = set(), []
    for s in adj:
        if s in seen: continue
        comp, stack = [], [s]
        seen.add(s)
        while stack:
            u = stack.pop(); comp.append(u)
            for v in adj.get(u, []):
                if v not in seen:
                    seen.add(v); stack.append(v)
        comps.append(sorted(comp))
    return comps

def is_bipartite(adj, comp):
    from collections import deque
    color = {}
    for s in comp:
        if s in color: continue
        color[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for v in adj.get(u, []):
                if v not in color:
                    color[v] = 1 - color[u]; q.append(v)
                elif color[v] == color[u]:
                    return False, color
    return True, color

adj = build_adj(EDGES)
for v in 'ABCDEFGHIKL': adj.setdefault(v, [])  # все вершины, вкл. изолированную H
comps = components(adj)
print('Компоненты связности:')
for c in comps:
    print(' ', c)
print('\nДвудольность каждой компоненты:')
for c in comps:
    ok, col = is_bipartite(adj, c)
    print(f'  {c}: {"двудольна" if ok else "НЕ двудольна"}', col if ok else '')
