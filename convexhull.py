def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(pts):
    pts = sorted(set(pts))
    if len(pts) <= 1: return pts
    lo = []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0: lo.pop()
        lo.append(p)
    hi = []
    for p in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= 0: hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]

def point_in_convex(hull, p):
    n = len(hull)
    if n < 3: return False
    if cross(hull[0], hull[1], p) < 0: return False
    if cross(hull[0], hull[-1], p) > 0: return False
    lo, hi = 1, n - 1
    while hi - lo > 1:
        m = (lo + hi) >> 1
        if cross(hull[0], hull[m], p) >= 0: lo = m
        else: hi = m
    return cross(hull[lo], hull[hi], p) >= 0
