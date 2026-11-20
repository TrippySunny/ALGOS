# Задание 3. MST электросети

EDGES = [
    (7, 1, 2), (4, 1, 3), (6, 1, 4),
    (9, 2, 3), (3, 2, 5), (2, 2, 6),
    (2, 5, 3),
    (5, 3, 4), (7, 4, 6), (5, 4, 7),
    (4, 5, 6), (6, 5, 8),
    (3, 6, 7), (3, 6, 7),
    (5, 6, 8), (2, 6, 8),
]
VERTS = [1, 2, 3, 4, 5, 6, 7, 8]

def kruskal(n, edges):
    parent = list(range(n + 1)); rank = [0] * (n + 1)
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
    for w, u, v in sorted(edges):
        if union(u, v):
            mst.append((u, v, w)); total += w
    return mst, total

def prim(n, edges, start=1):
    import heapq
    adj = {i: [] for i in VERTS}
    for w, u, v in edges:
        adj[u].append((v, w)); adj[v].append((u, w))
    in_mst = {start}; pq = [(w, start, v) for v, w in adj[start]]
    heapq.heapify(pq)
    mst, total = [], 0
    while pq and len(in_mst) < n:
        w, u, v = heapq.heappop(pq)
        if v in in_mst: continue
        in_mst.add(v); mst.append((u, v, w)); total += w
        for vv, ww in adj[v]:
            if vv not in in_mst:
                heapq.heappush(pq, (ww, v, vv))
    return mst, total

km, kt = kruskal(8, EDGES)
pm, pt = prim(8, EDGES, 1)
print('Краскал:', sorted(km), '| стоимость =', kt)
print('Прим   :', sorted(pm), '| стоимость =', pt)
print('Рёбер в MST:', len(km))
