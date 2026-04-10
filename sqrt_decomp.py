from math import isqrt

class SqrtDecomp:
    __slots__ = ('n', 'B', 'a', 'bl', 'nb')
    def __init__(s, a):
        s.n = len(a); s.B = max(1, isqrt(s.n)); s.a = list(a)
        s.nb = (s.n + s.B - 1) // s.B
        s.bl = [0] * s.nb
        for i in range(s.n): s.bl[i // s.B] += s.a[i]

    def update(s, i, v):
        s.bl[i // s.B] += v - s.a[i]; s.a[i] = v

    def add(s, i, v):
        s.bl[i // s.B] += v; s.a[i] += v

    def query(s, l, r):
        res = 0; lb = l // s.B; rb = r // s.B
        if lb == rb:
            for i in range(l, r + 1): res += s.a[i]
            return res
        for i in range(l, (lb + 1) * s.B): res += s.a[i]
        for b in range(lb + 1, rb): res += s.bl[b]
        for i in range(rb * s.B, r + 1): res += s.a[i]
        return res

class SqrtDecompLazy:
    __slots__ = ('n', 'B', 'a', 'bl', 'lz', 'nb')
    def __init__(s, a):
        s.n = len(a); s.B = max(1, isqrt(s.n)); s.a = list(a)
        s.nb = (s.n + s.B - 1) // s.B
        s.bl = [0] * s.nb; s.lz = [0] * s.nb
        for i in range(s.n): s.bl[i // s.B] += s.a[i]

    def range_add(s, l, r, v):
        lb = l // s.B; rb = r // s.B
        if lb == rb:
            for i in range(l, r + 1): s.a[i] += v
            s.bl[lb] += v * (r - l + 1)
            return
        for i in range(l, (lb + 1) * s.B): s.a[i] += v
        s.bl[lb] += v * ((lb + 1) * s.B - l)
        for b in range(lb + 1, rb): s.lz[b] += v; s.bl[b] += v * s.B
        for i in range(rb * s.B, r + 1): s.a[i] += v
        s.bl[rb] += v * (r - rb * s.B + 1)

    def query(s, l, r):
        res = 0; lb = l // s.B; rb = r // s.B
        if lb == rb:
            for i in range(l, r + 1): res += s.a[i] + s.lz[lb]
            return res
        for i in range(l, (lb + 1) * s.B): res += s.a[i] + s.lz[lb]
        for b in range(lb + 1, rb): res += s.bl[b]
        for i in range(rb * s.B, r + 1): res += s.a[i] + s.lz[rb]
        return res

    def point(s, i):
        return s.a[i] + s.lz[i // s.B]
