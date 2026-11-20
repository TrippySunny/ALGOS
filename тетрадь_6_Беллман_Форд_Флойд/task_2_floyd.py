# Задание 2. Флойд-Уоршелл: все пары вершин

EDGES = [
    (0, 1, 5),    # 1->2
    (0, 2, 10),   # 1->3
    (1, 2, 3),    # 2->3
    (1, 3, -2),   # 2->4  (подпись -2 видна один раз; направление 2->4)
    (3, 1, -2),   # 4->2  (на рисунке рёбра в обе стороны; вес -2)
    (2, 3, 2),    # 3->4
    (2, 4, 7),    # 3->5
    (3, 4, 4),    # 4->5
    (4, 0, 12),   # 5->1
]
N = 5
INF = float('inf')

def floyd_warshall(n, edges):
    d = [[INF] * n for _ in range(n)]
    nxt = [[None] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for u, v, w in edges:
        if w < d[u][v]:
            d[u][v] = w; nxt[u][v] = v
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    nxt[i][j] = nxt[i][k]
    return d, nxt

d, nxt = floyd_warshall(N, EDGES)
print('Матрица кратчайших расстояний:')
for row in d:
    print(['inf' if x == INF else x for x in row])

# восстановление пути i->j
def get_path(i, j):
    if d[i][j] == INF: return None
    path = [i]; seen = {i}
    while i != j:
        i = nxt[i][j]
        if i is None or i in seen: return path + ['...цикл...']
        seen.add(i); path.append(i)
    return path

print('\nПример пути 1->5 (0->4):', get_path(0, 4))
