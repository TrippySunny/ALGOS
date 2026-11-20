# Задание 2. A* в лабиринте 8×8

GRID = [
    'S..#....',
    '.#.#.##.',
    '.#.....#.',
    '.#####.#.',
    '....#...',
    '###.###.',
    '........',
    '.#####.G',
]

import heapq

def solve(grid, use_astar=True):
    R, C = len(grid), len(grid[0])
    s = g = None
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'S': s = (i, j)
            if grid[i][j] == 'G': g = (i, j)
    def h(p):
        return abs(p[0] - g[0]) + abs(p[1] - g[1]) if use_astar else 0
    openh = [(h(s), 0, s)]
    gs = {s: 0}; prev = {}; closed = set()
    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while openh:
        _, gc, u = heapq.heappop(openh)
        if u in closed: continue
        closed.add(u)
        if u == g: break
        for di, dj in DIRS:
            v = (u[0] + di, u[1] + dj)
            if 0 <= v[0] < R and 0 <= v[1] < C and grid[v[0]][v[1]] != '#':
                ng = gc + 1
                if ng < gs.get(v, float('inf')):
                    gs[v] = ng; prev[v] = u
                    heapq.heappush(openh, (ng + h(v), ng, v))
    path, u = [], g
    while u != s:
        path.append(u); u = prev[u]
    path.append(s)
    return path[::-1], gs[g], closed

path, cost, exp = solve(GRID, use_astar=True)
print('Путь A*:', path)
print('Длина пути:', cost)
print('Исследовано вершин A*:', len(exp))

path2, cost2, exp2 = solve(GRID, use_astar=False)  # h=0 -> Дейкстра
print('\nДля сравнения (Дейкстра, h=0):')
print('Длина пути:', cost2)
print('Исследовано вершин:', len(exp2))
