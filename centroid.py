def centroid_decomp(g):
    n = len(g)
    bfs = [n - 1]
    for u in bfs:
        bfs += g[u]
        for v in g[u]: g[v].remove(u)
    sz = [0] * n
    for u in reversed(bfs):
        sz[u] = 1 + sum(sz[c] for c in g[u])
    def reroot(r):
        N = sz[r]
        while True:
            for c in g[r]:
                if sz[c] > N // 2:
                    sz[r] = N - sz[c]; g[r].remove(c); g[c].append(r); r = c; break
            else: return r
    bfs2 = [n - 1]
    for u in bfs2:
        c = reroot(u); bfs2 += g[c]; yield c
