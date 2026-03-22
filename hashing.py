import random

HMOD = (1 << 61) - 1
HBASE = random.randrange(256, HMOD)

class HashStr:
    __slots__ = ('h', 'pw', 'n', 'mod', 'base')
    def __init__(s, t, mod=HMOD, base=HBASE):
        s.mod = mod; s.base = base; s.n = len(t)
        s.h = [0] * (s.n + 1); s.pw = [1] * (s.n + 1)
        for i in range(s.n):
            s.h[i + 1] = (s.h[i] * base + ord(t[i])) % mod
            s.pw[i + 1] = s.pw[i] * base % mod
    def get(s, l, r):
        return (s.h[r] - s.h[l] * s.pw[r - l]) % s.mod

class HashStrDouble:
    __slots__ = ('a', 'b')
    def __init__(s, t):
        s.a = HashStr(t); s.b = HashStr(t, (1 << 31) - 1, random.randrange(256, (1 << 31) - 1))
    def get(s, l, r):
        return (s.a.get(l, r), s.b.get(l, r))
