class LazySegAddSum:
    __slots__ = ('n', 'h', 't', 'lz')
    def __init__(s, a):
        s.n = len(a); s.h = s.n.bit_length()
        s.t = [0] * (2 * s.n); s.lz = [0] * s.n
        for i in range(s.n): s.t[s.n + i] = a[i]
        for i in range(s.n - 1, 0, -1): s.t[i] = s.t[2 * i] + s.t[2 * i + 1]
    def _apply(s, i, v, k):
        s.t[i] += v * k
        if i < s.n: s.lz[i] += v
    def _build(s, i):
        k = 2
        while i > 1: i >>= 1; s.t[i] = s.t[2 * i] + s.t[2 * i + 1] + s.lz[i] * k; k <<= 1
    def _push(s, i):
        for j in range(s.h, 0, -1):
            p = i >> j
            if s.lz[p]:
                k = 1 << (j - 1)
                s._apply(2 * p, s.lz[p], k); s._apply(2 * p + 1, s.lz[p], k)
                s.lz[p] = 0
    def update(s, l, r, v):
        l += s.n; r += s.n + 1; l0 = l; r0 = r; k = 1
        s._push(l0); s._push(r0 - 1)
        while l < r:
            if l & 1: s._apply(l, v, k); l += 1
            if r & 1: r -= 1; s._apply(r, v, k)
            l >>= 1; r >>= 1; k <<= 1
        s._build(l0); s._build(r0 - 1)
    def query(s, l, r):
        l += s.n; r += s.n + 1
        s._push(l); s._push(r - 1)
        a = 0
        while l < r:
            if l & 1: a += s.t[l]; l += 1
            if r & 1: r -= 1; a += s.t[r]
            l >>= 1; r >>= 1
        return a

class LazySegAddMax:
    __slots__ = ('n', 'h', 't', 'lz')
    def __init__(s, a):
        s.n = len(a); s.h = s.n.bit_length()
        s.t = [0] * (2 * s.n); s.lz = [0] * s.n
        for i in range(s.n): s.t[s.n + i] = a[i]
        for i in range(s.n - 1, 0, -1): s.t[i] = max(s.t[2 * i], s.t[2 * i + 1])
    def _apply(s, i, v):
        s.t[i] += v
        if i < s.n: s.lz[i] += v
    def _build(s, i):
        while i > 1: i >>= 1; s.t[i] = max(s.t[2 * i], s.t[2 * i + 1]) + s.lz[i]
    def _push(s, i):
        for j in range(s.h, 0, -1):
            p = i >> j
            if s.lz[p]:
                s._apply(2 * p, s.lz[p]); s._apply(2 * p + 1, s.lz[p])
                s.lz[p] = 0
    def update(s, l, r, v):
        l += s.n; r += s.n + 1; l0 = l; r0 = r
        s._push(l0); s._push(r0 - 1)
        while l < r:
            if l & 1: s._apply(l, v); l += 1
            if r & 1: r -= 1; s._apply(r, v)
            l >>= 1; r >>= 1
        s._build(l0); s._build(r0 - 1)
    def query(s, l, r):
        l += s.n; r += s.n + 1
        s._push(l); s._push(r - 1)
        a = float('-inf')
        while l < r:
            if l & 1: a = max(a, s.t[l]); l += 1
            if r & 1: r -= 1; a = max(a, s.t[r])
            l >>= 1; r >>= 1
        return a
