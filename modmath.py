MOD = 998244353

def modinv(a, m=MOD): return pow(a, m - 2, m)

class Comb:
    __slots__ = ('f', 'fi', 'm')
    def __init__(s, n, m=MOD):
        s.m = m; s.f = [1] * (n + 1); s.fi = [1] * (n + 1)
        for i in range(1, n + 1): s.f[i] = s.f[i - 1] * i % m
        s.fi[n] = pow(s.f[n], m - 2, m)
        for i in range(n - 1, -1, -1): s.fi[i] = s.fi[i + 1] * (i + 1) % m
    def nCr(s, n, r):
        if r < 0 or r > n: return 0
        return s.f[n] * s.fi[r] % s.m * s.fi[n - r] % s.m
    def nPr(s, n, r):
        if r < 0 or r > n: return 0
        return s.f[n] * s.fi[n - r] % s.m
    def nHr(s, n, r): return s.nCr(n + r - 1, r) if n else int(r == 0)

def sieve(n):
    is_p = bytearray(b'\x01') * (n + 1); is_p[0] = is_p[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            is_p[i*i::i] = bytearray(len(is_p[i*i::i]))
    return [i for i in range(2, n + 1) if is_p[i]]

def sieve_spf(n):
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j: spf[j] = i
    return spf

def factorize(n, spf=None):
    if spf:
        f = {}
        while n > 1: p = spf[n]; f[p] = f.get(p, 0) + 1; n //= p
        return f
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def crt(r1, m1, r2, m2):
    from math import gcd
    g = gcd(m1, m2)
    if (r2 - r1) % g: return -1, -1
    l = m1 // g * m2
    r = r1 + m1 * ((r2 - r1) // g * pow(m1 // g, m2 // g - 2, m2 // g) % (m2 // g))
    return r % l, l

def crt_list(rems, mods):
    r, m = 0, 1
    for ri, mi in zip(rems, mods):
        r, m = crt(r, m, ri, mi)
        if m == -1: return -1, -1
    return r, m
