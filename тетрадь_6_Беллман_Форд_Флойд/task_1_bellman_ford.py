# Задание 1. Беллман-Форд: кратчайшие пути от S

EDGES = [
    (0, 1, 4),   # S->A
    (0, 2, 3),   # S->B
    (1, 3, 7),   # A->C
    (1, 2, -2),  # A->B  (отрицательное ребро)
    (2, 3, 5),   # B->C
    (2, 4, 8),   # B->D
    (3, 4, -1),  # C->D  (отрицательное ребро)
    (3, 5, 6),   # C->T
    (4, 5, 3),   # D->T
]
N, SRC = 6, 0
INF = float('inf')

def bellman_ford(n, edges, s):
    dist = [INF] * n; prev = [None] * n
    dist[s] = 0
    # V-1 итераций: на каждой релаксируем все рёбра; prev нужен для восстановления пути
    for it in range(n - 1):
        changed = False
        for u, v, w in edges:
            # релаксация: если через u до v короче — обновляем метку
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w; prev[v] = u
                changed = True
                print(f'  итерация {it+1}: relax {u}->{v}, dist[{v}]={dist[v]}')
        if not changed:
            print(f'  итерация {it+1}: изменений нет — стоп')
            break
    neg = any(dist[u] != INF and dist[u] + w < dist[v] for u, v, w in edges)
    return dist, prev, neg

dist, prev, neg = bellman_ford(N, EDGES, SRC)
names = ['S', 'A', 'B', 'C', 'D', 'T']
print('\nКратчайшие расстояния от S:', {names[i]: dist[i] for i in range(N)})
print('Отрицательный цикл:', neg)

# путь S -> T
path, u = [], 5
while u is not None:
    path.append(names[u]); u = prev[u]
print('Путь S->T:', path[::-1])
