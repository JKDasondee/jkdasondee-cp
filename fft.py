MOD = 998244353; G = 3; GI = pow(3, MOD - 2, MOD)

def ntt(a, inv=False):
    n = len(a); j = 0
    for i in range(1, n):
        b = n >> 1
        while j & b: j ^= b; b >>= 1
        j ^= b
        if i < j: a[i], a[j] = a[j], a[i]
    l = 2
    while l <= n:
        w = pow(GI if inv else G, (MOD - 1) // l, MOD)
        for i in range(0, n, l):
            wn = 1
            for k in range(l // 2):
                u = a[i + k]; v = a[i + k + l // 2] * wn % MOD
                a[i + k] = (u + v) % MOD; a[i + k + l // 2] = (u - v) % MOD
                wn = wn * w % MOD
        l <<= 1
    if inv:
        ni = pow(n, MOD - 2, MOD)
        for i in range(n): a[i] = a[i] * ni % MOD

def poly_mul(a, b):
    n = 1; t = len(a) + len(b) - 1
    while n < t: n <<= 1
    a = a + [0] * (n - len(a)); b = b + [0] * (n - len(b))
    ntt(a); ntt(b)
    c = [x * y % MOD for x, y in zip(a, b)]
    ntt(c, inv=True)
    return c[:t]
