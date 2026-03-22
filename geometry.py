from math import hypot, atan2, pi

def dot(a, b): return a[0] * b[0] + a[1] * b[1]
def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def dist(a, b): return hypot(a[0] - b[0], a[1] - b[1])

def seg_intersect(a, b, c, d):
    d1 = cross(c, d, a); d2 = cross(c, d, b)
    d3 = cross(a, b, c); d4 = cross(a, b, d)
    if ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0)):
        t = d1 / (d1 - d2)
        return (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))
    return None

def line_intersect(p1, d1, p2, d2):
    c = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(c) < 1e-9: return None
    dx = p2[0] - p1[0]; dy = p2[1] - p1[1]
    t = (dx * d2[1] - dy * d2[0]) / c
    return (p1[0] + t * d1[0], p1[1] + t * d1[1])

def point_to_seg(p, a, b):
    ab = (b[0] - a[0], b[1] - a[1]); ap = (p[0] - a[0], p[1] - a[1])
    t = max(0, min(1, dot(ap, ab) / max(dot(ab, ab), 1e-18)))
    proj = (a[0] + t * ab[0], a[1] + t * ab[1])
    return dist(p, proj)

def polygon_area(pts):
    n = len(pts); a = 0
    for i in range(n): a += pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1]
    return abs(a) / 2

def point_in_polygon(p, poly):
    n = len(poly); c = 0
    for i in range(n):
        j = (i + 1) % n; a = poly[i]; b = poly[j]
        if (a[1] <= p[1] < b[1] or b[1] <= p[1] < a[1]) and p[0] < a[0] + (p[1] - a[1]) / (b[1] - a[1]) * (b[0] - a[0]):
            c ^= 1
    return c
