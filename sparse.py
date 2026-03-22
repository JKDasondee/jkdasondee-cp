class SparseTable:
    __slots__ = ('t', 'n', 'lg')
    def __init__(s, a):
        s.n = len(a)
        s.lg = [0] * (s.n + 1)
        for i in range(2, s.n + 1): s.lg[i] = s.lg[i >> 1] + 1
        k = s.lg[s.n] + 1 if s.n else 0
        s.t = [list(a)] + [None] * k
        for j in range(1, k + 1):
            p = s.t[j - 1]; h = 1 << (j - 1)
            s.t[j] = [min(p[i], p[i + h]) if i + h < s.n else p[i] for i in range(s.n)]
    def query(s, l, r):
        k = s.lg[r - l + 1]
        return min(s.t[k][l], s.t[k][r - (1 << k) + 1])
