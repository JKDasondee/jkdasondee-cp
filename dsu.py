class DSU:
    __slots__ = ('p', 'r')
    def __init__(s, n):
        s.p = list(range(n)); s.r = [0] * n
    def find(s, x):
        while s.p[x] != x: s.p[x] = s.p[s.p[x]]; x = s.p[x]
        return x
    def union(s, x, y):
        x = s.find(x); y = s.find(y)
        if x == y: return False
        if s.r[x] < s.r[y]: x, y = y, x
        s.p[y] = x
        if s.r[x] == s.r[y]: s.r[x] += 1
        return True

class WeightedDSU:
    __slots__ = ('p', 'r', 'w')
    def __init__(s, n):
        s.p = list(range(n)); s.r = [0] * n; s.w = [0] * n
    def find(s, x):
        if s.p[x] == x: return x, 0
        r, d = s.find(s.p[x])
        s.p[x] = r; s.w[x] += d
        return r, s.w[x]
    def union(s, x, y, d):
        rx, dx = s.find(x); ry, dy = s.find(y)
        if rx == ry: return dx - dy == d
        if s.r[rx] < s.r[ry]: rx, ry = ry, rx; d = -d; dx, dy = dy, dx
        s.p[ry] = rx; s.w[ry] = dx - dy + d
        if s.r[rx] == s.r[ry]: s.r[rx] += 1
        return True
    def dist(s, x, y):
        rx, dx = s.find(x); ry, dy = s.find(y)
        if rx != ry: return None
        return dy - dx
