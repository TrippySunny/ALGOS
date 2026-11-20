# Задание 1. Эйлеровость и алгоритм Флёри

EDGES = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'E'),
    ('C', 'D'), ('C', 'E'), ('C', 'F'), ('D', 'F'), ('E', 'F'),
    ('E', 'G'), ('F', 'G'),
]

from collections import defaultdict, deque

def is_bridge(adj, u, v):
    # временно удаляем ребро u-v и проверяем, достижима ли v из u
    adj[u].remove(v); adj[v].remove(u)
    seen, q = {u}, deque([u])
    while q:
        x = q.popleft()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); q.append(y)
    adj[u].append(v); adj[v].append(u)
    return v not in seen

def fleury(adj, start):
    # идём от start; на каждом шаге берём не-мост, если есть выбор
    path, u = [start], start
    while adj[u]:
        nxt = None
        for v in adj[u]:
            if len(adj[u]) == 1 or not is_bridge(adj, u, v):
                nxt = v
                break
        if nxt is None:
            nxt = adj[u][0]
        adj[u].remove(nxt); adj[nxt].remove(u)
        path.append(nxt); u = nxt
    return path

adj = defaultdict(list)
for u, v in EDGES:
    adj[u].append(v); adj[v].append(u)

deg = {v: len(ns) for v, ns in adj.items()}
odd = [v for v, d in deg.items() if d % 2 == 1]
print('Степени вершин:', deg)
print('Нечётные вершины:', odd)
print('Всего рёбер:', sum(len(ns) for ns in adj.values()) // 2)

if not odd:
    print('Граф ЭЙЛЕРОВ -> ищем цикл Флёри:')
    cyc = fleury(adj, sorted(adj)[0])
    print('Цикл:', ' -> '.join(cyc))
elif len(odd) == 2:
    print('Граф ПОЛУЭЙЛЕРОВ -> путь от', odd[0], 'до', odd[1])
    p = fleury(adj, odd[0])
    print('Путь:', ' -> '.join(p))
else:
    print('Граф ни эйлеров, ни полуэйлеров')
