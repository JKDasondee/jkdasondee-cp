def z_function(s):
    n = len(s); z = [0] * n; z[0] = n; l = r = 0
    for i in range(1, n):
        if i < r: z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]: z[i] += 1
        if i + z[i] > r: l = i; r = i + z[i]
    return z

def kmp(s):
    n = len(s); f = [0] * n; k = 0
    for i in range(1, n):
        while k and s[k] != s[i]: k = f[k - 1]
        if s[k] == s[i]: k += 1
        f[i] = k
    return f

def manacher(s):
    n = len(s)
    d1 = [0] * n; l = r = 0
    for i in range(n):
        d1[i] = max(0, min(r - i, d1[l + r - i])) if i < r else 0
        while i - d1[i] >= 0 and i + d1[i] < n and s[i - d1[i]] == s[i + d1[i]]: d1[i] += 1
        if i + d1[i] > r: l = i - d1[i] + 1; r = i + d1[i]
    d2 = [0] * n; l = r = 0
    for i in range(n):
        d2[i] = max(0, min(r - i, d2[l + r - i - 1])) if i < r else 0
        while i - d2[i] - 1 >= 0 and i + d2[i] < n and s[i - d2[i] - 1] == s[i + d2[i]]: d2[i] += 1
        if i + d2[i] > r: l = i - d2[i]; r = i + d2[i]
    return d1, d2

def suffix_array(s):
    n = len(s); sa = list(range(n)); rk = [ord(c) for c in s]; tmp = [0] * n
    k = 1
    while k < n:
        def cmp_key(i): return (rk[i], rk[i + k] if i + k < n else -1)
        sa.sort(key=cmp_key)
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]] + (1 if cmp_key(sa[i]) != cmp_key(sa[i - 1]) else 0)
        rk = tmp[:]; k <<= 1
        if rk[sa[-1]] == n - 1: break
    return sa

def lcp_array(s, sa):
    n = len(s); rk = [0] * n
    for i in range(n): rk[sa[i]] = i
    lcp = [0] * (n - 1); h = 0
    for i in range(n):
        if rk[i] == 0: h = 0; continue
        j = sa[rk[i] - 1]
        while i + h < n and j + h < n and s[i + h] == s[j + h]: h += 1
        lcp[rk[i] - 1] = h
        if h > 0: h -= 1
    return lcp
