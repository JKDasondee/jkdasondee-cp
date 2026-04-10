from math import gcd, isqrt
from random import randint

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    d = n - 1; r = 0
    while d % 2 == 0: d >>= 1; r += 1
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if a >= n: continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1: break
        else:
            return False
    return True

def pollard_rho(n):
    if n % 2 == 0: return 2
    while True:
        x = randint(2, n - 1); y = x; c = randint(1, n - 1); d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n; y = (y * y + c) % n
            d = gcd(abs(x - y), n)
        if d != n: return d

def factorize(n):
    if n <= 1: return {}
    if is_prime(n): return {n: 1}
    d = pollard_rho(n)
    f1 = factorize(d); f2 = factorize(n // d)
    for p, e in f2.items(): f1[p] = f1.get(p, 0) + e
    return f1

def divisors(n):
    f = factorize(n); d = [1]
    for p, e in f.items():
        nd = []
        for x in d:
            pk = 1
            for _ in range(e + 1): nd.append(x * pk); pk *= p
        d = nd
    return sorted(d)
