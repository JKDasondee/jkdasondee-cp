def mat_mul(A, B, mod):
    n = len(A); m = len(B[0]); k = len(B)
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            s = 0
            for p in range(k): s += A[i][p] * B[p][j]
            C[i][j] = s % mod
    return C

def mat_pow(M, p, mod):
    n = len(M); R = [[int(i == j) for j in range(n)] for i in range(n)]
    while p:
        if p & 1: R = mat_mul(R, M, mod)
        M = mat_mul(M, M, mod); p >>= 1
    return R

def linear_rec(coefs, init, n, mod=998244353):
    k = len(coefs)
    if n < k: return init[n]
    M = [[0] * k for _ in range(k)]
    for j in range(k): M[0][j] = coefs[j]
    for i in range(1, k): M[i][i - 1] = 1
    R = mat_pow(M, n - k + 1, mod)
    return sum(R[0][j] * init[k - 1 - j] for j in range(k)) % mod
