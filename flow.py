from collections import deque

class Dinic:
    __slots__ = ('n', 'g', 'lv', 'it')
    def __init__(s, n):
        s.n = n; s.g = [[] for _ in range(n)]
    def add(s, u, v, c):
        s.g[u].append([v, c, len(s.g[v])])
        s.g[v].append([u, 0, len(s.g[u]) - 1])
    def _bfs(s, src):
        s.lv = [-1] * s.n; s.lv[src] = 0; q = deque([src])
        while q:
            u = q.popleft()
            for v, c, _ in s.g[u]:
                if c > 0 and s.lv[v] < 0: s.lv[v] = s.lv[u] + 1; q.append(v)
    def _dfs(s, u, snk, f):
        if u == snk: return f
        while s.it[u] < len(s.g[u]):
            e = s.g[u][s.it[u]]; v, c, r = e
            if c > 0 and s.lv[v] == s.lv[u] + 1:
                d = s._dfs(v, snk, min(f, c))
                if d > 0: e[1] -= d; s.g[v][r][1] += d; return d
            s.it[u] += 1
        return 0
    def max_flow(s, src, snk):
        f = 0
        while True:
            s._bfs(src)
            if s.lv[snk] < 0: return f
            s.it = [0] * s.n
            while True:
                d = s._dfs(src, snk, float('inf'))
                if d == 0: break
                f += d

class MCMF:
    __slots__ = ('n', 'g')
    def __init__(s, n):
        s.n = n; s.g = [[] for _ in range(n)]
    def add(s, u, v, cap, cost):
        s.g[u].append([v, cap, cost, len(s.g[v])])
        s.g[v].append([u, 0, -cost, len(s.g[u]) - 1])
    def min_cost_flow(s, src, snk, max_flow=float('inf')):
        flow = cost = 0
        while flow < max_flow:
            d = [float('inf')] * s.n; d[src] = 0
            inq = [0] * s.n; inq[src] = 1
            pv = [-1] * s.n; pe = [-1] * s.n
            q = deque([src])
            while q:
                u = q.popleft(); inq[u] = 0
                for i, (v, c, w, _) in enumerate(s.g[u]):
                    if c > 0 and d[u] + w < d[v]:
                        d[v] = d[u] + w; pv[v] = u; pe[v] = i
                        if not inq[v]: inq[v] = 1; q.append(v)
            if d[snk] == float('inf'): break
            f = max_flow - flow; v = snk
            while v != src: f = min(f, s.g[pv[v]][pe[v]][1]); v = pv[v]
            flow += f; cost += f * d[snk]; v = snk
            while v != src:
                e = s.g[pv[v]][pe[v]]; e[1] -= f; s.g[v][e[3]][1] += f; v = pv[v]
        return flow, cost
