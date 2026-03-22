class SegTree:
    __slots__ = ('n', 't', 'op', 'e')
    def __init__(s, a, op, e):
        s.n = len(a); s.op = op; s.e = e
        s.t = [e] * (2 * s.n)
        for i in range(s.n): s.t[s.n + i] = a[i]
        for i in range(s.n - 1, 0, -1): s.t[i] = op(s.t[2 * i], s.t[2 * i + 1])
    def update(s, i, v):
        i += s.n; s.t[i] = v
        while i > 1: i >>= 1; s.t[i] = s.op(s.t[2 * i], s.t[2 * i + 1])
    def query(s, l, r):
        a = b = s.e; l += s.n; r += s.n + 1
        while l < r:
            if l & 1: a = s.op(a, s.t[l]); l += 1
            if r & 1: r -= 1; b = s.op(s.t[r], b)
            l >>= 1; r >>= 1
        return s.op(a, b)

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

class SegMin:
    __slots__ = ('n', 't')
    def __init__(s, a):
        s.n = len(a); s.t = [float('inf')] * (2 * s.n)
        for i in range(s.n): s.t[s.n + i] = a[i]
        for i in range(s.n - 1, 0, -1): s.t[i] = min(s.t[2 * i], s.t[2 * i + 1])
    def update(s, i, v):
        i += s.n; s.t[i] = v
        while i > 1: i >>= 1; s.t[i] = min(s.t[2 * i], s.t[2 * i + 1])
    def query(s, l, r):
        a = float('inf'); l += s.n; r += s.n + 1
        while l < r:
            if l & 1: a = min(a, s.t[l]); l += 1
            if r & 1: r -= 1; a = min(a, s.t[r])
            l >>= 1; r >>= 1
        return a
