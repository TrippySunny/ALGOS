# Задание 3. A* с заданной эвристикой

EDGES = [
    ('A', 'B', 2), ('A', 'C', 4), ('B', 'D', 5), ('C', 'D', 1),
    ('D', 'F', 3), ('C', 'E', 7), ('E', 'F', 2), ('E', 'G', 6),
    ('F', 'H', 4), ('G', 'H', 3), ('H', 'T', 5),
]
H = {
    'A': 8, 'B': 7, 'C': 6, 'D': 5, 'E': 4, 'F': 3, 'G': 3, 'H': 2, 'T': 0,
}

import heapq

adj = {}
for u, v, w in EDGES:
    adj.setdefault(u, []).append((v, w))
    adj.setdefault(v, []).append((u, w))

# 1) Проверка допустимости: для каждого ребра h(u) <= w(u,v) + h(v)
print('Проверка допустимости эвристики:')
all_ok = True
for u in adj:
    for v, w in adj[u]:
        if H[u] > w + H[v]:
            all_ok = False
            print(f'  НЕДОПУСТИМО на ребре {u}-{v}: h({u})={H[u]} > {w}+h({v})={w + H[v]}')
if all_ok:
    print('  Эвристика допустима (согласована) для всех рёбер')

def astar(s, t, hfun):
    openh = [(hfun(s), 0, s)]
    g = {s: 0}; prev = {}; closed = set()
    while openh:
        _, gc, u = heapq.heappop(openh)
        if u in closed: continue
        closed.add(u)
        if u == t: break
        for v, w in adj.get(u, []):
            ng = gc + w
            if ng < g.get(v, float('inf')):
                g[v] = ng; prev[v] = u
                heapq.heappush(openh, (ng + hfun(v), ng, v))
    path, u = [], t
    while u != s:
        path.append(u); u = prev[u]
    path.append(s)
    return path[::-1], g[t], closed

path1, c1, e1 = astar('A', 'T', lambda v: H[v])
path2, c2, e2 = astar('A', 'T', lambda v: 0)
print('\nA* с заданной h: путь', path1, '| стоимость', c1, '| исследовано', len(e1))
print('A* с h=0 (Дейкстра): путь', path2, '| стоимость', c2, '| исследовано', len(e2))
