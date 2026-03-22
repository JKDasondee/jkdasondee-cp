class LiChao:
    __slots__ = ('lo', 'hi', 'lc', 'rc', 'a', 'b', 'sz')
    def __init__(s, lo, hi):
        s.lo = lo; s.hi = hi
        s.lc = [0]; s.rc = [0]
        s.a = [0]; s.b = [float('inf')]
        s.sz = 1
    def _node(s):
        s.lc.append(0); s.rc.append(0)
        s.a.append(0); s.b.append(float('inf'))
        n = s.sz; s.sz += 1; return n
    def _f(s, i, x): return s.a[i] * x + s.b[i]
    def add(s, a, b, lo=None, hi=None, u=0):
        if lo is None: lo = s.lo; hi = s.hi
        if lo == hi:
            if a * lo + b < s._f(u, lo): s.a[u] = a; s.b[u] = b
            return
        m = (lo + hi) >> 1
        lf = a * lo + b < s._f(u, lo)
        mf = a * m + b < s._f(u, m)
        if mf: s.a[u], a = a, s.a[u]; s.b[u], b = b, s.b[u]
        if lf != mf:
            if not s.lc[u]: s.lc[u] = s._node()
            s.add(a, b, lo, m, s.lc[u])
        else:
            if not s.rc[u]: s.rc[u] = s._node()
            s.add(a, b, m + 1, hi, s.rc[u])
    def query(s, x, lo=None, hi=None, u=0):
        if lo is None: lo = s.lo; hi = s.hi
        r = s._f(u, x)
        if lo == hi: return r
        m = (lo + hi) >> 1
        if x <= m and s.lc[u]: r = min(r, s.query(x, lo, m, s.lc[u]))
        elif x > m and s.rc[u]: r = min(r, s.query(x, m + 1, hi, s.rc[u]))
        return r
