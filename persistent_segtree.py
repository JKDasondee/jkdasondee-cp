class PersistentSeg:
    __slots__ = ('lc', 'rc', 'v')
    def __init__(s, sz=0):
        s.lc = [0] * (sz or 1); s.rc = [0] * (sz or 1); s.v = [0] * (sz or 1)
        s.lc[0] = s.rc[0] = s.v[0] = 0

    def _new(s, l, r, v):
        i = len(s.v)
        s.lc.append(l); s.rc.append(r); s.v.append(v)
        return i

    def build(s, a, lo, hi):
        if lo == hi: return s._new(0, 0, a[lo])
        m = (lo + hi) >> 1
        l = s.build(a, lo, m); r = s.build(a, m + 1, hi)
        return s._new(l, r, s.v[l] + s.v[r])

    def update(s, p, lo, hi, i, v):
        if lo == hi: return s._new(0, 0, s.v[p] + v)
        m = (lo + hi) >> 1
        if i <= m:
            nl = s.update(s.lc[p], lo, m, i, v)
            return s._new(nl, s.rc[p], s.v[nl] + s.v[s.rc[p]])
        else:
            nr = s.update(s.rc[p], m + 1, hi, i, v)
            return s._new(s.lc[p], nr, s.v[s.lc[p]] + s.v[nr])

    def query(s, p, lo, hi, ql, qr):
        if ql <= lo and hi <= qr: return s.v[p]
        if qr < lo or hi < ql: return 0
        m = (lo + hi) >> 1
        return s.query(s.lc[p], lo, m, ql, qr) + s.query(s.rc[p], m + 1, hi, ql, qr)

    def kth(s, lp, rp, lo, hi, k):
        if lo == hi: return lo
        m = (lo + hi) >> 1
        cnt = s.v[s.lc[rp]] - s.v[s.lc[lp]]
        if k <= cnt: return s.kth(s.lc[lp], s.lc[rp], lo, m, k)
        return s.kth(s.rc[lp], s.rc[rp], m + 1, hi, k - cnt)
