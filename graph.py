from heapq import heappush, heappop
from collections import deque

def dijkstra(g, s):
    n = len(g); d = [float('inf')] * n; d[s] = 0; h = [(0, s)]
    while h:
        c, u = heappop(h)
        if c > d[u]: continue
        for v, w in g[u]:
            if d[u] + w < d[v]: d[v] = d[u] + w; heappush(h, (d[v], v))
    return d

def bfs(g, s):
    n = len(g); d = [-1] * n; d[s] = 0; q = deque([s])
    while q:
        u = q.popleft()
        for v in g[u]:
            if d[v] == -1: d[v] = d[u] + 1; q.append(v)
    return d

def bfs01(g, s):
    n = len(g); d = [float('inf')] * n; d[s] = 0; q = deque([s])
    while q:
        u = q.popleft()
        for v, w in g[u]:
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                if w == 0: q.appendleft(v)
                else: q.append(v)
    return d

def toposort(g, n):
    deg = [0] * n
    for u in range(n):
        for v in g[u]: deg[v] += 1
    q = deque(u for u in range(n) if deg[u] == 0); r = []
    while q:
        u = q.popleft(); r.append(u)
        for v in g[u]:
            deg[v] -= 1
            if deg[v] == 0: q.append(v)
    return r if len(r) == n else []

def scc_tarjan(g, n):
    idx = [0]; order = [0] * n; low = [0] * n; on = [0] * n
    stk = []; comp = [-1] * n; scc = []
    for i in range(n):
        if order[i]: continue
        call = [(i, 0)]
        while call:
            u, j = call.pop()
            if j == 0:
                idx[0] += 1; order[u] = low[u] = idx[0]; stk.append(u); on[u] = 1
            if j < len(g[u]):
                call.append((u, j + 1)); v = g[u][j]
                if not order[v]: call.append((v, 0))
                elif on[v]: low[u] = min(low[u], order[v])
            else:
                if order[u] == low[u]:
                    c = []
                    while True:
                        v = stk.pop(); on[v] = 0; comp[v] = len(scc); c.append(v)
                        if v == u: break
                    scc.append(c)
                if call:
                    p = call[-1][0]; low[p] = min(low[p], low[u])
    return scc, comp

def bridges(g, n):
    idx = [0]; order = [0] * n; low = [0] * n; br = []
    for i in range(n):
        if order[i]: continue
        call = [(i, -1, 0)]
        while call:
            u, par, j = call.pop()
            if j == 0: idx[0] += 1; order[u] = low[u] = idx[0]
            if j < len(g[u]):
                call.append((u, par, j + 1)); v = g[u][j]
                if not order[v]: call.append((v, u, 0))
                elif v != par: low[u] = min(low[u], order[v])
            else:
                if par != -1:
                    low[par] = min(low[par], low[u])
                    if low[u] > order[par]: br.append((par, u))
    return br

def articulation_points(g, n):
    idx = [0]; order = [0] * n; low = [0] * n; ap = set(); ch_cnt = [0] * n
    for i in range(n):
        if order[i]: continue
        call = [(i, -1, 0)]
        while call:
            u, par, j = call.pop()
            if j == 0: idx[0] += 1; order[u] = low[u] = idx[0]
            if j < len(g[u]):
                call.append((u, par, j + 1)); v = g[u][j]
                if not order[v]: call.append((v, u, 0))
                elif v != par: low[u] = min(low[u], order[v])
            else:
                if par != -1:
                    low[par] = min(low[par], low[u])
                    if par == i: ch_cnt[i] += 1
                    elif low[u] >= order[par]: ap.add(par)
        if ch_cnt[i] > 1: ap.add(i)
    return ap
