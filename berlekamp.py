MOD = 998244353

def berlekamp_massey(s, mod=MOD):
    n = len(s); L = m = 0
    C = [0] * (n + 1); B = [0] * (n + 1); T = []
    C[0] = B[0] = 1; b = 1
    for i in range(n):
        m += 1; d = s[i] % mod
        for j in range(1, L + 1): d = (d + C[j] * s[i - j]) % mod
        if not d: continue
        T = C[:]; coef = d * pow(b, mod - 2, mod) % mod
        for j in range(m, n): C[j] = (C[j] - coef * B[j - m]) % mod
        if 2 * L > i: continue
        L = i + 1 - L; B, b, m = T[:], d, 0
    return [-C[i] % mod for i in range(1, L + 1)]

def linear_rec(S, tr, k, mod=MOD):
    n = len(S)
    def combine(a, b):
        res = [0] * (2 * n + 1)
        for i in range(n + 1):
            for j in range(n + 1): res[i + j] = (res[i + j] + a[i] * b[j]) % mod
        for i in range(2 * n, n, -1):
            for j in range(n): res[i - 1 - j] = (res[i - 1 - j] + res[i] * tr[j]) % mod
        return res[:n + 1]
    pol = [0] * (n + 1); e = [0] * (n + 1); pol[0] = e[1] = 1; k += 1
    while k:
        if k & 1: pol = combine(pol, e)
        e = combine(e, e); k >>= 1
    return sum(pol[i + 1] * S[i] for i in range(n)) % mod
