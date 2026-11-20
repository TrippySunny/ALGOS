# Задание 2. MST сети между городами

CITIES = ['SPb', 'NNovgorod', 'Moscow', 'Kazan', 'Ufa',
          'Ekaterinburg', 'Tyumen', 'Samara', 'Volgograd', 'Rostov', 'Krasnodar']
EDGES = [
    ('SPb', 'NNovgorod', 1200), ('SPb', 'Moscow', 650),
    ('Moscow', 'NNovgorod', 400), ('NNovgorod', 'Kazan', 400),
    ('Moscow', 'Kazan', 800), ('Kazan', 'Ufa', 500),
    ('Ufa', 'Ekaterinburg', 550), ('Ekaterinburg', 'Tyumen', 350),
    ('Kazan', 'Samara', 450), ('Ufa', 'Samara', 450),
    ('Moscow', 'Rostov', 1100), ('Samara', 'Volgograd', 850),
    ('Samara', 'Rostov', 900), ('Rostov', 'Volgograd', 400),
    ('Rostov', 'Krasnodar', 250),
]

def kruskal(cities, edges):
    parent = {c: c for c in cities}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb: return False
        parent[rb] = ra
        return True
    mst, total = [], 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if union(u, v):
            mst.append((u, v, w)); total += w
    return mst, total

mst, total = kruskal(CITIES, EDGES)
print('MST (Краскал):')
for u, v, w in mst:
    print(f'  {u} — {v}: {w} км')
print('Общая длина сети:', total, 'км')
print('Рёбер в MST:', len(mst), '(ожидается', len(CITIES) - 1, ')')

# Центральные города — наибольшая степень в MST
from collections import Counter
deg = Counter()
for u, v, w in mst:
    deg[u] += 1; deg[v] += 1
print('Степени вершин MST:', dict(deg))
print('Центральные города:', [c for c, d in deg.most_common(3)])

# Новая дорога Москва-Казань 500 км: добавьте ребро и перезапустите
# ('Москва', 'Казань', 500) — если 500 меньше максимального ребра
# на пути между ними в текущем MST, оно войдёт в MST.
