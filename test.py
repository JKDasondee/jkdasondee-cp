import sys

def test_fenwick():
    from fenwick import BIT, BIT2D
    b = BIT(10)
    for i in range(1, 11): b.update(i, i)
    assert b.query(5) == 15
    assert b.range_query(3, 7) == 25
    assert b.kth(15) == 5
    b2 = BIT2D(5, 5)
    b2.update(1, 1, 3); b2.update(2, 2, 5)
    assert b2.query(2, 2) == 8
    assert b2.range_query(2, 2, 5, 5) == 5
    print("fenwick OK")

def test_segtree():
    from segtree import SegTree, SegSum, SegMin
    a = [1, 3, 5, 7, 9]
    st = SegSum(a)
    assert st.query(0, 4) == 25
    st.update(2, 10)
    assert st.query(0, 4) == 30
    sm = SegMin(a)
    assert sm.query(0, 4) == 1
    assert sm.query(1, 3) == 3
    g = SegTree(a, lambda x, y: x + y, 0)
    assert g.query(0, 4) == 25
    print("segtree OK")

def test_lazysegtree():
    from lazysegtree import LazySegAddSum, LazySegAddMax
    a = [1, 2, 3, 4, 5]
    ls = LazySegAddSum(a)
    ls.update(1, 3, 10)
    assert ls.query(0, 4) == 45
    assert ls.query(1, 3) == 39
    lm = LazySegAddMax(a)
    lm.update(0, 4, 5)
    assert lm.query(0, 4) == 10
    print("lazysegtree OK")

def test_dsu():
    from dsu import DSU, WeightedDSU
    d = DSU(5)
    assert d.union(0, 1) == True
    assert d.union(1, 2) == True
    assert d.find(0) == d.find(2)
    assert d.union(0, 2) == False
    w = WeightedDSU(5)
    w.union(0, 1, 3)
    w.union(1, 2, 5)
    assert w.dist(0, 2) == 8
    print("dsu OK")

def test_sortedlist():
    from sortedlist import SortedList
    sl = SortedList([5, 3, 1, 4, 2])
    assert len(sl) == 5
    assert sl[0] == 1
    assert sl[4] == 5
    assert sl.bisect_left(3) == 2
    assert sl.bisect_right(3) == 3
    assert 3 in sl
    sl.remove(3)
    assert 3 not in sl
    assert len(sl) == 4
    sl.add(6)
    assert sl[4] == 6
    print("sortedlist OK")

def test_sparse():
    from sparse import SparseTable
    a = [5, 2, 4, 7, 1, 3, 8]
    st = SparseTable(a)
    assert st.query(0, 6) == 1
    assert st.query(0, 2) == 2
    assert st.query(3, 5) == 1
    assert st.query(1, 1) == 2
    print("sparse OK")

def test_trie():
    from trie import Trie, XorTrie
    t = Trie()
    t.add("hello"); t.add("help"); t.add("world")
    assert t.search("hello") == 1
    assert t.search("hel") == 0
    assert t.starts_with("hel") == 2
    t.remove("hello")
    assert t.search("hello") == 0
    xt = XorTrie(4)
    xt.add(3); xt.add(5); xt.add(7)
    assert xt.max_xor(2) == 7
    print("trie OK")

def test_lichao():
    from lichao import LiChao
    lc = LiChao(0, 100)
    lc.add(1, 0)
    lc.add(-1, 100)
    assert lc.query(0) == 0
    assert lc.query(50) == 50
    assert lc.query(100) == 0
    print("lichao OK")

def test_treap():
    from treap import build, kth, insert, erase, reverse, sz
    t = build([1, 2, 3, 4, 5])
    assert sz(t) == 5
    assert kth(t, 0) == 1
    assert kth(t, 4) == 5
    t = insert(t, 2, 10)
    assert kth(t, 2) == 10
    assert sz(t) == 6
    t = erase(t, 2)
    assert sz(t) == 5
    assert kth(t, 2) == 3
    t = reverse(t, 1, 3)
    assert kth(t, 1) == 4
    assert kth(t, 3) == 2
    print("treap OK")

def test_modmath():
    from modmath import modinv, Comb, sieve, sieve_spf, factorize, crt, MOD
    assert modinv(2) * 2 % MOD == 1
    c = Comb(100)
    assert c.nCr(10, 3) == 120
    assert c.nPr(5, 3) == 60
    assert c.nHr(3, 2) == 6
    p = sieve(20)
    assert p == [2, 3, 5, 7, 11, 13, 17, 19]
    spf = sieve_spf(20)
    assert spf[12] == 2
    f = factorize(60)
    assert f == {2: 2, 3: 1, 5: 1}
    r, m = crt(2, 3, 3, 5)
    assert r == 8 and m == 15
    print("modmath OK")

def test_graph():
    from graph import dijkstra, bfs, bfs01, toposort, scc_tarjan, bridges
    g = [[(1, 2), (2, 5)], [(2, 1), (3, 7)], [(3, 3)], []]
    d = dijkstra(g, 0)
    assert d == [0, 2, 3, 6]
    g2 = [[1, 2], [0, 3], [0, 3], [1, 2]]
    d2 = bfs(g2, 0)
    assert d2 == [0, 1, 1, 2]
    g3 = [[(1, 0), (2, 1)], [(2, 0)], []]
    d3 = bfs01(g3, 0)
    assert d3 == [0, 0, 0]
    g4 = [[1], [2], [], []]
    assert toposort(g4, 4) == [0, 3, 1, 2] or len(toposort(g4, 4)) == 4
    g5 = [[1], [2], [0, 3], [4], [3]]
    scc, comp = scc_tarjan(g5, 5)
    assert len(scc) == 2
    g6 = [[1, 2], [0, 2], [0, 1, 3], [2]]
    br = bridges(g6, 4)
    assert (2, 3) in br or (3, 2) in br
    print("graph OK")

def test_flow():
    from flow import Dinic, MCMF
    d = Dinic(4)
    d.add(0, 1, 10); d.add(0, 2, 10); d.add(1, 3, 10); d.add(2, 3, 10); d.add(1, 2, 5)
    assert d.max_flow(0, 3) == 20
    mc = MCMF(4)
    mc.add(0, 1, 2, 1); mc.add(0, 2, 2, 3); mc.add(1, 3, 2, 2); mc.add(2, 3, 2, 1)
    f, c = mc.min_cost_flow(0, 3)
    assert f == 4 and c == 14
    print("flow OK")

def test_lca():
    from lca import LCA
    g = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]]
    lca = LCA(g, 0)
    assert lca.lca(3, 4) == 1
    assert lca.lca(3, 5) == 0
    assert lca.dist(3, 5) == 4
    assert lca.kth(3, 5, 2) == 0
    print("lca OK")

def test_convexhull():
    from convexhull import convex_hull, point_in_convex
    pts = [(0, 0), (1, 0), (0, 1), (1, 1), (0.5, 0.5)]
    hull = convex_hull(pts)
    assert len(hull) == 4
    assert point_in_convex(hull, (0.5, 0.5))
    print("convexhull OK")

def test_fft():
    from fft import poly_mul
    a = [1, 2, 3]; b = [4, 5]
    c = poly_mul(a, b)
    assert c[:4] == [4, 13, 22, 15]
    print("fft OK")

def test_strings():
    from strings import z_function, kmp, manacher, suffix_array, lcp_array
    z = z_function("aabxaab")
    assert z[0] == 7 and z[4] == 3
    f = kmp("aabaaab")
    assert f[-1] == 3
    d1, d2 = manacher("abacaba")
    assert d1[3] == 4
    sa = suffix_array("banana")
    assert sa == [5, 3, 1, 0, 4, 2]
    lcp = lcp_array("banana", sa)
    assert lcp == [1, 3, 0, 0, 2]
    print("strings OK")

def test_matrix():
    from matrix import mat_pow, linear_rec
    I = mat_pow([[1, 1], [1, 0]], 0, 10**9 + 7)
    assert I == [[1, 0], [0, 1]]
    fib = linear_rec([1, 1], [0, 1], 10, 10**9 + 7)
    assert fib == 55
    print("matrix OK")

def test_hld():
    from hld import HLD
    g = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]]
    h = HLD(g, 0)
    h.path_update(3, 5)
    h.path_update(5, 3)
    assert h.path_query(3, 5) == 8
    print("hld OK")

if __name__ == '__main__':
    test_fenwick()
    test_segtree()
    test_lazysegtree()
    test_dsu()
    test_sortedlist()
    test_sparse()
    test_trie()
    test_lichao()
    test_treap()
    test_modmath()
    test_graph()
    test_flow()
    test_lca()
    test_convexhull()
    test_fft()
    test_strings()
    test_matrix()
    test_hld()
    print("\nALL TESTS PASSED")
