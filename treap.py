from random import randint

class Treap:
    __slots__ = ('v', 'p', 'sz', 'rv', 'l', 'r')
    def __init__(s, v=0):
        s.v = v; s.p = randint(0, (1 << 62)); s.sz = 1; s.rv = False; s.l = None; s.r = None

def sz(t): return t.sz if t else 0

def pull(t):
    if t: t.sz = sz(t.l) + 1 + sz(t.r)

def push(t):
    if t and t.rv:
        t.l, t.r = t.r, t.l
        if t.l: t.l.rv ^= True
        if t.r: t.r.rv ^= True
        t.rv = False

def split(t, k):
    if not t: return None, None
    push(t)
    if sz(t.l) < k:
        t.r, b = split(t.r, k - sz(t.l) - 1)
        pull(t); return t, b
    else:
        a, t.l = split(t.l, k)
        pull(t); return a, t

def merge(a, b):
    if not a or not b: return a or b
    push(a); push(b)
    if a.p > b.p:
        a.r = merge(a.r, b); pull(a); return a
    else:
        b.l = merge(a, b.l); pull(b); return b

def insert(t, k, v):
    a, b = split(t, k)
    return merge(merge(a, Treap(v)), b)

def erase(t, k):
    a, b = split(t, k); _, b = split(b, 1)
    return merge(a, b)

def reverse(t, l, r):
    a, b = split(t, l); b, c = split(b, r - l + 1)
    b.rv ^= True
    return merge(merge(a, b), c)

def kth(t, k):
    push(t)
    if sz(t.l) == k: return t.v
    if k < sz(t.l): return kth(t.l, k)
    return kth(t.r, k - sz(t.l) - 1)

def build(a):
    t = None
    for v in a: t = merge(t, Treap(v))
    return t
