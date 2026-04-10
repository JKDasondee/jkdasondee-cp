class XorBasis:
    __slots__ = ('b', 'sz')
    def __init__(s, bits=60):
        s.b = [0] * bits; s.sz = 0

    def insert(s, x):
        for i in range(len(s.b) - 1, -1, -1):
            if not (x >> i & 1): continue
            if not s.b[i]: s.b[i] = x; s.sz += 1; return True
            x ^= s.b[i]
        return False

    def max_xor(s, x=0):
        for i in range(len(s.b) - 1, -1, -1):
            x = max(x, x ^ s.b[i])
        return x

    def min_xor(s, x=0):
        for i in range(len(s.b) - 1, -1, -1):
            if s.b[i] and (x >> i & 1): x ^= s.b[i]
        return x

    def can_rep(s, x):
        for i in range(len(s.b) - 1, -1, -1):
            if x >> i & 1:
                if not s.b[i]: return False
                x ^= s.b[i]
        return True

    def kth(s, k):
        rb = []
        for i in range(len(s.b)):
            if s.b[i]:
                for j in range(i):
                    if s.b[i] >> j & 1 and s.b[j]: s.b[i] ^= s.b[j]
                rb.append(s.b[i])
        if k > (1 << len(rb)) - 1: return -1
        r = 0
        for i in range(len(rb)):
            if k >> i & 1: r ^= rb[i]
        return r
