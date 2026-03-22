class BIT:
    __slots__ = ('n', 't')
    def __init__(s, n):
        s.n = n; s.t = [0] * (n + 1)
    def update(s, i, d):
        while i <= s.n: s.t[i] += d; i += i & -i
    def query(s, i):
        r = 0
        while i > 0: r += s.t[i]; i &= i - 1
        return r
    def range_query(s, l, r): return s.query(r) - s.query(l - 1)
    def kth(s, k):
        p = 0; b = 1
        while b <= s.n: b <<= 1
        b >>= 1
        while b:
            if p + b <= s.n and s.t[p + b] < k: p += b; k -= s.t[p]
            b >>= 1
        return p + 1

class BIT2D:
    __slots__ = ('n', 'm', 't')
    def __init__(s, n, m):
        s.n = n; s.m = m; s.t = [[0] * (m + 1) for _ in range(n + 1)]
    def update(s, x, y, d):
        i = x
        while i <= s.n:
            j = y
            while j <= s.m: s.t[i][j] += d; j += j & -j
            i += i & -i
    def query(s, x, y):
        r = 0; i = x
        while i > 0:
            j = y
            while j > 0: r += s.t[i][j]; j -= j & -j
            i -= i & -i
        return r
    def range_query(s, x1, y1, x2, y2):
        return s.query(x2, y2) - s.query(x1 - 1, y2) - s.query(x2, y1 - 1) + s.query(x1 - 1, y1 - 1)
