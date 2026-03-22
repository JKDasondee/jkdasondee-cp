class Trie:
    __slots__ = ('ch', 'cnt', 'end', 'sz')
    def __init__(s):
        s.ch = [{}]; s.cnt = [0]; s.end = [0]; s.sz = 1
    def _node(s):
        s.ch.append({}); s.cnt.append(0); s.end.append(0)
        n = s.sz; s.sz += 1; return n
    def add(s, w):
        u = 0
        for c in w:
            if c not in s.ch[u]: s.ch[u][c] = s._node()
            u = s.ch[u][c]; s.cnt[u] += 1
        s.end[u] += 1
    def search(s, w):
        u = 0
        for c in w:
            if c not in s.ch[u]: return 0
            u = s.ch[u][c]
        return s.end[u]
    def starts_with(s, w):
        u = 0
        for c in w:
            if c not in s.ch[u]: return 0
            u = s.ch[u][c]
        return s.cnt[u]
    def remove(s, w):
        u = 0; path = [u]
        for c in w:
            if c not in s.ch[u]: return False
            u = s.ch[u][c]; path.append(u)
        if not s.end[u]: return False
        s.end[u] -= 1
        for v in path: s.cnt[v] -= 1
        return True

class XorTrie:
    __slots__ = ('ch', 'cnt', 'B')
    def __init__(s, B=30):
        s.B = B; s.ch = [[0, 0]]; s.cnt = [0]
    def _node(s):
        s.ch.append([0, 0]); s.cnt.append(0)
        return len(s.ch) - 1
    def add(s, x):
        u = 0
        for i in range(s.B, -1, -1):
            b = (x >> i) & 1
            if not s.ch[u][b]: s.ch[u][b] = s._node()
            u = s.ch[u][b]; s.cnt[u] += 1
    def remove(s, x):
        u = 0
        for i in range(s.B, -1, -1):
            b = (x >> i) & 1; u = s.ch[u][b]; s.cnt[u] -= 1
    def max_xor(s, x):
        u = 0; r = 0
        for i in range(s.B, -1, -1):
            b = (x >> i) & 1; w = 1 - b
            if s.ch[u][w] and s.cnt[s.ch[u][w]] > 0:
                r |= 1 << i; u = s.ch[u][w]
            else:
                u = s.ch[u][b]
        return r
