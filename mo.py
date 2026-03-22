from math import isqrt

def mo(n, queries, add, rem, ans):
    B = max(1, isqrt(n))
    qs = sorted(range(len(queries)), key=lambda i: (queries[i][0] // B, queries[i][1] if (queries[i][0] // B) % 2 == 0 else -queries[i][1]))
    cl = cr = 0; res = [0] * len(queries)
    for i in qs:
        l, r = queries[i]
        while cr < r: add(cr); cr += 1
        while cl > l: cl -= 1; add(cl)
        while cr > r: cr -= 1; rem(cr)
        while cl < l: rem(cl); cl += 1
        res[i] = ans()
    return res
