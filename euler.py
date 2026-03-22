from collections import defaultdict

def euler_path(n, edges):
    g = defaultdict(list); deg = [0] * n
    for i, (u, v) in enumerate(edges):
        g[u].append((v, i)); g[v].append((u, i)); deg[u] += 1; deg[v] += 1
    odds = [i for i in range(n) if deg[i] % 2]
    if len(odds) > 2: return None
    s = odds[0] if odds else next(i for i in range(n) if deg[i] > 0)
    used = [0] * len(edges); idx = {u: 0 for u in range(n)}
    stk = [s]; path = []
    while stk:
        u = stk[-1]
        while idx[u] < len(g[u]) and used[g[u][idx[u]][1]]: idx[u] += 1
        if idx[u] == len(g[u]):
            path.append(stk.pop())
        else:
            v, ei = g[u][idx[u]]; used[ei] = 1; idx[u] += 1; stk.append(v)
    return path[::-1] if len(path) == len(edges) + 1 else None

def euler_path_directed(n, edges):
    g = defaultdict(list); ind = [0] * n; outd = [0] * n
    for i, (u, v) in enumerate(edges):
        g[u].append((v, i)); outd[u] += 1; ind[v] += 1
    start = end = -1
    for i in range(n):
        if outd[i] - ind[i] == 1:
            if start != -1: return None
            start = i
        elif ind[i] - outd[i] == 1:
            if end != -1: return None
            end = i
        elif ind[i] != outd[i]: return None
    if start == -1: start = next((i for i in range(n) if outd[i] > 0), 0)
    idx = {u: 0 for u in range(n)}; stk = [start]; path = []
    while stk:
        u = stk[-1]
        if idx.get(u, 0) < len(g[u]):
            v, _ = g[u][idx[u]]; idx[u] += 1; stk.append(v)
        else: path.append(stk.pop())
    return path[::-1] if len(path) == len(edges) + 1 else None
