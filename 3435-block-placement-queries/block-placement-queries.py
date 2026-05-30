from bisect import bisect_right
from typing import List

class SegTree:
    def __init__(self, n):
        self.n = n
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)
    
    def update(self, idx, val):
        idx += self.size
        self.tree[idx] = val
        idx >>= 1
        while idx:
            self.tree[idx] = max(self.tree[idx << 1], self.tree[idx << 1 | 1])
            idx >>= 1
    
    def query(self, l, r):
        if l > r:
            return 0
        res = 0
        l += self.size
        r += self.size
        while l <= r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if not (r & 1):
                res = max(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Coordinate compression
        coords = set()
        for q in queries:
            if q[0] == 1:
                coords.add(q[1])
            else:
                coords.add(q[1])
        coords.add(0)
        coords = sorted(coords)
        coord_to_idx = {v: i for i, v in enumerate(coords)}
        n = len(coords)
        
        seg = SegTree(n)
        obstacles = [0]
        
        # Initialize all gaps to 0
        for i in range(n):
            seg.update(i, 0)
        
        res = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                pos = bisect_right(obstacles, x)
                left = obstacles[pos - 1]
                right = obstacles[pos] if pos < len(obstacles) else None
                
                # Update gap ending at x
                seg.update(coord_to_idx[x], x - left)
                
                # Update gap ending at right
                if right is not None:
                    seg.update(coord_to_idx[right], right - x)
                
                obstacles.insert(pos, x)
            else:
                _, x, sz = q
                pos = bisect_right(obstacles, x) - 1
                last_obstacle = obstacles[pos]
                
                # Check the last segment
                if x - last_obstacle >= sz:
                    res.append(True)
                    continue
                
                # Find max gap ending at or before x
                # Find the index of the largest coordinate <= x
                idx = bisect_right(coords, x) - 1
                if idx >= 0:
                    max_gap = seg.query(0, idx)
                    res.append(max_gap >= sz)
                else:
                    res.append(False)
        
        return res