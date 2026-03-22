from collections import deque

class LCA:
    __slots__ = ('n', 'LOG', 'up', 'dep')
    def __init__(s, g, root=0):
        s.n = len(g); s.LOG = max(1, s.n.bit_length())
        s.up = [[0] * s.n for _ in range(s.LOG)]
        s.dep = [0] * s.n
        q = deque([root]); vis = [0] * s.n; vis[root] = 1
        while q:
            u = q.popleft()
            for v in g[u]:
                if not vis[v]:
                    vis[v] = 1; s.dep[v] = s.dep[u] + 1; s.up[0][v] = u; q.append(v)
        for k in range(1, s.LOG):
            for v in range(s.n): s.up[k][v] = s.up[k - 1][s.up[k - 1][v]]
    def lca(s, u, v):
        if s.dep[u] < s.dep[v]: u, v = v, u
        d = s.dep[u] - s.dep[v]
        for k in range(s.LOG):
            if (d >> k) & 1: u = s.up[k][u]
        if u == v: return u
        for k in range(s.LOG - 1, -1, -1):
            if s.up[k][u] != s.up[k][v]: u = s.up[k][u]; v = s.up[k][v]
        return s.up[0][u]
    def dist(s, u, v): return s.dep[u] + s.dep[v] - 2 * s.dep[s.lca(u, v)]
    def kth(s, u, v, k):
        w = s.lca(u, v)
        du = s.dep[u] - s.dep[w]; dv = s.dep[v] - s.dep[w]
        if k <= du:
            x = u
            for i in range(s.LOG):
                if (k >> i) & 1: x = s.up[i][x]
            return x
        k = du + dv - k; x = v
        for i in range(s.LOG):
            if (k >> i) & 1: x = s.up[i][x]
        return x
