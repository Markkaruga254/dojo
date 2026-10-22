# Pattern templates (Python)

Read the idea, then **retype it from memory** the next day.

## Hash map counting / complement
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
```

## Two pointers (sorted)
```python
def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        if s < target:
            l += 1
        else:
            r -= 1
    return []
```

## Sliding window (variable)
```python
def longest_unique(s):
    last, left, best = {}, 0, 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best
```

## Binary search on the answer
```python
def min_speed(piles, h):          # "smallest x such that feasible(x)"
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if sum((p + mid - 1) // mid for p in piles) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
```
Use `bisect.bisect_left / bisect_right` for plain sorted-array lookups.

## Monotonic stack
```python
def daily_temperatures(t):
    res, st = [0] * len(t), []
    for i, x in enumerate(t):
        while st and t[st[-1]] < x:
            j = st.pop()
            res[j] = i - j
        st.append(i)
    return res
```

## Heap: top-k
```python
import heapq

def top_k(nums, k):               # O(n log k)
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return sorted(h, reverse=True)
```

## Intervals
```python
def merge(intervals):
    intervals.sort()
    out = []
    for s, e in intervals:
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out
```

## Trie
```python
class Trie:
    def __init__(self):
        self.kids, self.end = {}, False

    def insert(self, w):
        n = self
        for ch in w:
            n = n.kids.setdefault(ch, Trie())
        n.end = True

    def _walk(self, s):
        n = self
        for ch in s:
            n = n.kids.get(ch)
            if n is None:
                return None
        return n

    def search(self, w):
        n = self._walk(w)
        return bool(n and n.end)

    def starts_with(self, p):
        return self._walk(p) is not None
```

## BFS / DFS on a graph
```python
from collections import deque

def bfs(graph, start):
    seen, q, order = {start}, deque([start]), []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v not in seen:
                seen.add(v)
                q.append(v)
    return order

def dfs_iter(graph, start):
    seen, stack, order = set(), [start], []
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        order.append(u)
        stack.extend(reversed(graph.get(u, [])))
    return order
```
Grids: treat `(r, c)` as nodes; neighbours are the 4 directions inside bounds.

## Topological sort (Kahn)
```python
from collections import deque

def topo(n, edges):
    adj, indeg = [[] for _ in range(n)], [0] * n
    for a, b in edges:
        adj[a].append(b)
        indeg[b] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []   # [] means a cycle
```

## Union-Find
```python
class DSU:
    def __init__(self, n):
        self.p, self.sz = list(range(n)), [1] * n

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        self.sz[ra] += self.sz[rb]
        return True
```

## Dijkstra
```python
import heapq

def dijkstra(graph, src):          # graph: {u: [(v, w), ...]}, w >= 0
    dist, pq = {src: 0}, [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float("inf")):
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

## Backtracking
```python
def subsets(nums):
    res, path = [], []
    def dfs(i):
        if i == len(nums):
            res.append(path[:])
            return
        path.append(nums[i]); dfs(i + 1); path.pop()   # take
        dfs(i + 1)                                      # skip
    dfs(0)
    return res
```
Template: choose → recurse → un-choose. Prune early. Dedupe by sorting + skipping equal siblings.

## Dynamic programming
```python
from functools import lru_cache

def coin_change(coins, amount):
    @lru_cache(None)
    def f(rem):
        if rem == 0:
            return 0
        if rem < 0:
            return float("inf")
        return 1 + min((f(rem - c) for c in coins), default=float("inf"))
    ans = f(amount)
    return -1 if ans == float("inf") else ans
```
Recipe: define the state in words → recurrence → base cases → memoise → convert to a table if needed → shrink space.

## Complexity cheat-sheet (CPython)
list append O(1) amortised · `x in list` O(n) · `x in set/dict` O(1) avg · `list.pop(0)` O(n) (use `deque`) · slicing O(k) · `sorted` O(n log n) · `heapq` push/pop O(log n).
