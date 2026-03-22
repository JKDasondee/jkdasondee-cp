import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right, insort
from itertools import accumulate, permutations, combinations, product
from functools import lru_cache, reduce
from math import gcd, lcm, isqrt, comb, log2, ceil, floor, inf

input = sys.stdin.buffer.read().decode()
_i = 0

def rd():
    global _i
    while _i < len(input) and input[_i] <= ' ': _i += 1
    j = _i
    while _i < len(input) and input[_i] > ' ': _i += 1
    return input[j:_i]

def ri(): return int(rd())
def rs(): return rd()
def rf(): return float(rd())
def rl(n): return [ri() for _ in range(n)]

def main():
    out = []
    pr = out.append
    t = ri()
    for _ in range(t):
        n = ri()
        a = rl(n)
        pr(str(0))
    sys.stdout.write('\n'.join(out))

main()
