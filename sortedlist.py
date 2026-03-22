from bisect import bisect_left, bisect_right, insort
from math import isqrt

class SortedList:
    __slots__ = ('bk', 'sz', 'bs')
    def __init__(s, a=None, bs=0):
        if a is None: a = []
        a = sorted(a)
        s.bs = bs or max(isqrt(len(a)), 700)
        s.bk = [a[i:i + s.bs] for i in range(0, len(a), s.bs)] or [[]]
        s.sz = len(a)
    def _loc(s, v):
        for i, b in enumerate(s.bk):
            if not b or v <= b[-1]: return i
        return len(s.bk) - 1
    def _split(s, i):
        if len(s.bk[i]) > 2 * s.bs:
            m = len(s.bk[i]) // 2
            s.bk.insert(i + 1, s.bk[i][m:])
            s.bk[i] = s.bk[i][:m]
    def add(s, v):
        i = s._loc(v); insort(s.bk[i], v); s.sz += 1; s._split(i)
    def remove(s, v):
        i = s._loc(v); b = s.bk[i]
        j = bisect_left(b, v)
        if j < len(b) and b[j] == v:
            b.pop(j); s.sz -= 1
            if not b and len(s.bk) > 1: s.bk.pop(i)
            return True
        return False
    def __contains__(s, v):
        i = s._loc(v); b = s.bk[i]; j = bisect_left(b, v)
        return j < len(b) and b[j] == v
    def __len__(s): return s.sz
    def __getitem__(s, k):
        if k < 0: k += s.sz
        for b in s.bk:
            if k < len(b): return b[k]
            k -= len(b)
        raise IndexError
    def bisect_left(s, v):
        r = 0
        for b in s.bk:
            if not b or v <= b[-1]: return r + bisect_left(b, v)
            r += len(b)
        return r
    def bisect_right(s, v):
        r = 0
        for b in s.bk:
            if not b or v <= b[-1]: return r + bisect_right(b, v)
            r += len(b)
        return r
    def kth(s, k): return s[k]
    def count(s, v): return s.bisect_right(v) - s.bisect_left(v)
