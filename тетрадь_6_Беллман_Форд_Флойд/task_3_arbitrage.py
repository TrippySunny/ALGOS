# Задание 3. Арбитраж валют (Беллман-Форд)

RATES = {
    'USD': {'EUR': 0.85, 'JPY': 145},
    'EUR': {'GBP': 1.15},
    'GBP': {'USD': 1.05, 'JPY': 0.0075},
    'JPY': {},
}
START = 'EUR'
CAPITAL = 1000
import math

def find_arbitrage(rates, start):
    curr = list(rates)
    idx = {c: i for i, c in enumerate(curr)}
    edges = [(idx[u], idx[v], -math.log(r))
             for u, outs in rates.items() for v, r in outs.items()]
    n = len(curr); INF = float('inf')
    dist = [INF] * n; prev = [None] * n
    dist[idx[start]] = 0
    x = None
    for it in range(n):
        x = None
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w; prev[v] = u; x = v
        if x is None:
            print('Арбитража нет')
            return
    y = x
    for _ in range(n):
        y = prev[y]
    cyc = [curr[y]]; u = prev[y]
    while u != y:
        cyc.append(curr[u]); u = prev[u]
    cyc.append(curr[y]); cyc.reverse()
    print('Арбитражный цикл:', ' -> '.join(cyc), '->', cyc[0])
    prod = 1.0
    for a, b in zip(cyc, cyc[1:]):
        prod *= rates[a][b]
    print(f'Произведение курсов: {prod:.6f}')
    print(f'Прибыль при капитале {CAPITAL}: {CAPITAL * prod - CAPITAL:.2f} '
          f'({(prod - 1) * 100:.2f}%)')

find_arbitrage(RATES, START)
