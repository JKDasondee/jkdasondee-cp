from collections import deque

class AhoCorasick:
    __slots__ = ('goto', 'fail', 'out', 'sz')
    def __init__(s):
        s.goto = [{}]; s.fail = [0]; s.out = [[]]; s.sz = 1
    def add(s, pat, idx=0):
        u = 0
        for c in pat:
            if c not in s.goto[u]:
                s.goto[u][c] = s.sz; s.goto.append({}); s.fail.append(0); s.out.append([]); s.sz += 1
            u = s.goto[u][c]
        s.out[u].append(idx)
    def build(s):
        q = deque()
        for c, v in s.goto[0].items(): q.append(v)
        while q:
            u = q.popleft()
            for c, v in s.goto[u].items():
                q.append(v); f = s.fail[u]
                while f and c not in s.goto[f]: f = s.fail[f]
                s.fail[v] = s.goto[f].get(c, 0)
                if s.fail[v] == v: s.fail[v] = 0
                s.out[v] = s.out[v] + s.out[s.fail[v]]
    def search(s, text):
        u = 0; res = []
        for i, c in enumerate(text):
            while u and c not in s.goto[u]: u = s.fail[u]
            u = s.goto[u].get(c, 0)
            if s.out[u]: res.append((i, s.out[u]))
        return res
