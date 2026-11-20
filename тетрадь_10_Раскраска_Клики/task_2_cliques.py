# Задание 2. Клики и независимые множества

EDGES = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'C'), ('B', 'D'), ('C', 'D'),
    ('C', 'E'), ('D', 'F'), ('E', 'F'), ('E', 'G'), ('F', 'G'), ('F', 'H'), ('G', 'H'),
]

from collections import defaultdict

def bron_kerbosch(R, P, X, adj, out):
    # R — текущая клика, P — кандидаты на расширение, X — уже отвергнутые
    # пивот u уменьшает перебор: рассматриваем только P \ N(u)
    if not P and not X:
        out.append(R); return
    u = max(P | X, key=lambda v: len(adj[v] & P), default=None)
    for v in list(P - (adj[u] if u else set())):
        bron_kerbosch(R | {v}, P & adj[v], X & adj[v], adj, out)
        P = P - {v}; X = X | {v}

def max_cliques(adj):
    out = []
    bron_kerbosch(set(), set(adj), set(), adj, out)
    return out

adj = defaultdict(set)
for u, v in EDGES:
    adj[u].add(v); adj[v].add(u)

cliques = max_cliques(adj)
big = max(cliques, key=len)
print('Максимальные клики:', [sorted(c) for c in cliques])
print('Наибольшая клика (размер %d):' % len(big), sorted(big))
print('Нижняя оценка χ(G) >=', len(big))

# дополнение графа
comp = defaultdict(set)
V = sorted(adj)
for i, u in enumerate(V):
    for v in V[i + 1:]:
        if v not in adj[u]:
            comp[u].add(v); comp[v].add(u)

mis = max_cliques(comp)
print('\nМаксимальные независимые множества (= клики дополнения):')
for m in mis:
    print(' ', sorted(m))
