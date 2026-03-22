class TwoSat:
    __slots__ = ('n', 'g')
    def __init__(s, n):
        s.n = n; s.g = [[] for _ in range(2 * n)]
    def _imp(s, x, y):
        s.g[x].append(y if y >= 0 else 2 * s.n + y)
    def either(s, x, y):
        s._imp(~x, y); s._imp(~y, x)
    def set(s, x):
        s._imp(~x, x)
    def solve(s):
        g = s.g; n2 = 2 * s.n
        scc, S, P = [], [], []
        d = [0] * n2; stk = list(range(n2))
        while stk:
            u = stk.pop()
            if u < 0:
                v = ~u; dep = d[v] - 1
                if P[-1] > dep:
                    scc.append(S[dep:]); del S[dep:], P[-1]
                    for x in scc[-1]: d[x] = -1
            elif d[u] > 0:
                while P[-1] > d[u]: P.pop()
            elif d[u] == 0:
                S.append(u); P.append(len(S)); d[u] = len(S)
                stk.append(~u); stk += g[u]
        scc.reverse()
        ord_ = [0] * n2
        for i, c in enumerate(scc):
            for x in c: ord_[x] = i
        for i in range(s.n):
            if ord_[i] == ord_[~i]: return None
        return [+(ord_[i] > ord_[~i]) for i in range(s.n)]
