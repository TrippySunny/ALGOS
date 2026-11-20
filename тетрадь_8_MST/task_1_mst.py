# Задание 1. MST графа A–H (Краскал и Прим)

EDGES = [
    (6, 'A', 'B'), (4, 'A', 'C'), (8, 'A', 'D'),
    (2, 'B', 'C'), (7, 'B', 'E'), (3, 'C', 'D'),
    (5, 'D', 'F'), (6, 'D', 'G'), (4, 'E', 'F'), (3, 'E', 'H'),
    (2, 'F', 'G'), (8, 'F', 'H'), (5, 'G', 'H'),
    (5, 'B', 'F'), (5, 'E', 'D'),
]
VERTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def kruskal(n, edges):
    idx = {v: i for i, v in enumerate(VERTS)}
    parent = list(range(n)); rank = [0] * n
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb: return False
        if rank[ra] < rank[rb]: ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]: rank[ra] += 1
        return True
    mst, total = [], 0
    # идём по рёбрам от меньшего веса к большему; union-find не даёт создать цикл
    for w, u, v in sorted(edges):
        if union(idx[u], idx[v]):
            mst.append((u, v, w)); total += w
    return mst, total

def prim(n, edges, start='A'):
    adj = {v: [] for v in VERTS}
    for w, u, v in edges:
        adj[u].append((v, w)); adj[v].append((u, w))
    import heapq
    in_mst = {start}; pq = [(w, start, v) for v, w in adj[start]]
    heapq.heapify(pq)
    mst, total = [], 0
    # каждый шаг добавляем ребро минимального веса к ещё не включённой вершине
    while pq and len(in_mst) < n:
        w, u, v = heapq.heappop(pq)
        if v in in_mst: continue
        in_mst.add(v); mst.append((u, v, w)); total += w
        for vv, ww in adj[v]:
            if vv not in in_mst:
                heapq.heappush(pq, (ww, v, vv))
    return mst, total

km, kt = kruskal(8, EDGES)
pm, pt = prim(8, EDGES, 'A')
print('Краскал:', sorted(km), '| вес =', kt)
print('Прим  :', sorted(pm), '| вес =', pt)
print('Совпадают:', kt == pt)

# Разрез для одного ребра MST (например, (A,C,4)): удаляем его из дерева —
# вершины разбиваются на 2 компоненты, это и есть разрез (S, V\S)
import collections
madj = collections.defaultdict(list)
for u, v, w in km:
    madj[u].append(v); madj[v].append(u)

e = km[0]  # берём первое ребро MST
u0, v0, w0 = e
madj[u0].remove(v0); madj[v0].remove(u0)
seen, q = {u0}, collections.deque([u0])
while q:
    x = q.popleft()
    for y in madj[x]:
        if y not in seen:
            seen.add(y); q.append(y)
S = seen
cross = [x for x in EDGES if (x[1] in S) != (x[2] in S)]
print(f'Ребро {e}: разрез S={sorted(S)}, V\\S={sorted(set(VERTS)-S)}')
print('Рёбра через разрез:', cross, '| минимальное:', min(cross, key=lambda x: x[0]))
