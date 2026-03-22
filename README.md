# jkdasondee-cp

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![PyPy](https://img.shields.io/badge/PyPy-3-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Personal competitive programming library. Pajenegod-style Python.

**JKDasondee** — CodeChef 6★ | LeetCode Guardian | AtCoder GR93

## Templates

| File | Description |
|------|-------------|
| `template.py` | Master contest template with fast I/O |
| `interactive.py` | Interactive problem template with flush |
| `fenwick.py` | BIT: point update, prefix/range query, kth element, 2D |
| `segtree.py` | Iterative segment tree: generic, sum, min |
| `lazysegtree.py` | Lazy segment tree: add+sum, add+max |
| `dsu.py` | DSU with path compression + rank, weighted DSU |
| `sortedlist.py` | SortedList via sqrt decomposition |
| `sparse.py` | Sparse table for static RMQ, O(1) query |
| `trie.py` | String trie + XOR bitwise trie |
| `lichao.py` | Li Chao tree for convex hull trick |
| `treap.py` | Implicit treap: split/merge, reverse, kth |
| `modmath.py` | MOD arithmetic, Comb, sieve, factorize, CRT |
| `graph.py` | Dijkstra, BFS, 0-1 BFS, toposort, SCC, bridges, articulation |
| `flow.py` | Dinic's max flow, min cost max flow (SPFA) |
| `lca.py` | LCA with binary lifting, dist, kth ancestor |
| `convexhull.py` | Andrew's monotone chain, point-in-convex-polygon |
| `fft.py` | NTT (mod 998244353), polynomial multiplication |
| `strings.py` | Z-function, KMP, Manacher, suffix array + LCP |
| `matrix.py` | Matrix exponentiation, linear recurrences |
| `hld.py` | Heavy-Light Decomposition with segment tree |
| `aho.py` | Aho-Corasick automaton: multi-pattern matching |
| `twosat.py` | 2-SAT solver via SCC |
| `centroid.py` | Centroid decomposition (generator-based) |
| `bootstrap.py` | Recursion limit bypass decorator |
| `hashing.py` | Polynomial string hashing (mod 2^61-1, double hash) |
| `mo.py` | Mo's algorithm for offline range queries |
| `berlekamp.py` | Berlekamp-Massey + kth term of linear recurrence |
| `euler.py` | Euler path/circuit (undirected + directed) |
| `geometry.py` | Segment/line intersection, point-to-seg, polygon area, PIP |
| `misc.py` | LIS, coordinate compression, run-length encoding |

## Usage

Copy-paste the relevant class/function directly into your contest submission. Each file is standalone — no cross-file dependencies.

```python
# Example: paste BIT into your solution
class BIT:
    __slots__ = ('n', 't')
    def __init__(s, n):
        s.n = n; s.t = [0] * (n + 1)
    # ... rest of BIT
```

## Style

- No comments, no docstrings, no type hints
- `s` instead of `self`, short variable names
- `__slots__` on all classes
- Iterative over recursive
- Optimized for PyPy 3 on Codeforces/AtCoder

## Credit

Inspired by [PyRival](https://github.com/cheran-senthil/PyRival).

## License

MIT — JKDasondee 2026
