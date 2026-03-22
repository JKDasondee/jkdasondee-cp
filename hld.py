from collections import deque

class HLD:
    __slots__ = ('n', 'par', 'dep', 'sz', 'top', 'pos', 'head', 'seg')
    def __init__(s, g, root=0):
        s.n = len(g)
        s.par = [-1] * s.n; s.dep = [0] * s.n; s.sz = [1] * s.n
        s.top = [0] * s.n; s.pos = [0] * s.n; s.head = [0] * s.n
        order = []; q = deque([root]); vis = [0] * s.n; vis[root] = 1
        while q:
            u = q.popleft(); order.append(u)
            for v in g[u]:
                if not vis[v]: vis[v] = 1; s.par[v] = u; s.dep[v] = s.dep[u] + 1; q.append(v)
        for u in reversed(order):
            for v in g[u]:
                if v != s.par[u]: s.sz[u] += s.sz[v]
        t = 0
        stk = [root]
        while stk:
            u = stk.pop()
            s.pos[u] = t; t += 1
            hv = -1; hs = 0
            for v in g[u]:
                if v != s.par[u] and s.sz[v] > hs: hv = v; hs = s.sz[v]
            ch = []
            for v in g[u]:
                if v != s.par[u] and v != hv: ch.append(v)
            for v in reversed(ch): s.head[v] = v; stk.append(v)
            if hv != -1: s.head[hv] = s.head[u]; stk.append(hv)
        s.seg = SegSum([0] * s.n)
    def _path(s, u, v):
        r = []
        while s.head[u] != s.head[v]:
            if s.dep[s.head[u]] < s.dep[s.head[v]]: u, v = v, u
            r.append((s.pos[s.head[u]], s.pos[u])); u = s.par[s.head[u]]
        if s.dep[u] > s.dep[v]: u, v = v, u
        r.append((s.pos[u], s.pos[v]))
        return r
    def path_query(s, u, v):
        r = 0
        for l, ri in s._path(u, v): r += s.seg.query(l, ri)
        return r
    def path_update(s, u, val): s.seg.update(s.pos[u], val)

class SegSum:
    __slots__ = ('n', 't')
    def __init__(s, a):
        s.n = len(a); s.t = [0] * (2 * s.n)
        for i in range(s.n): s.t[s.n + i] = a[i]
        for i in range(s.n - 1, 0, -1): s.t[i] = s.t[2 * i] + s.t[2 * i + 1]
    def update(s, i, v):
        i += s.n; s.t[i] = v
        while i > 1: i >>= 1; s.t[i] = s.t[2 * i] + s.t[2 * i + 1]
    def query(s, l, r):
        a = 0; l += s.n; r += s.n + 1
        while l < r:
            if l & 1: a += s.t[l]; l += 1
            if r & 1: r -= 1; a += s.t[r]
            l >>= 1; r >>= 1
        return a
