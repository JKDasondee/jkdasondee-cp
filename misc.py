def lis(a):
    from bisect import bisect_left
    d = []
    for x in a:
        p = bisect_left(d, x)
        if p == len(d): d.append(x)
        else: d[p] = x
    return len(d)

def lis_full(a):
    from bisect import bisect_left
    d = []; pos = []; par = [-1] * len(a); idx = []
    for i, x in enumerate(a):
        p = bisect_left(d, x)
        if p == len(d): d.append(x); idx.append(i)
        else: d[p] = x; idx[p] = i
        pos.append(p)
        par[i] = idx[p - 1] if p > 0 else -1
    res = []; k = idx[len(d) - 1]
    while k != -1: res.append(a[k]); k = par[k]
    return res[::-1]

def compress(a):
    s = sorted(set(a)); d = {v: i for i, v in enumerate(s)}
    return [d[x] for x in a], s

def run_length(a):
    if not a: return []
    res = [(a[0], 1)]
    for i in range(1, len(a)):
        if a[i] == res[-1][0]: res[-1] = (res[-1][0], res[-1][1] + 1)
        else: res.append((a[i], 1))
    return res
