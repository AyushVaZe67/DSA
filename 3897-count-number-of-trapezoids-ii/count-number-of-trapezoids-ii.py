from typing import List
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        INF = 1e9 + 7

        slopeIntercpts = defaultdict(list)
        midPointMap = defaultdict(list)

        result = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                # Compute slope & intercept
                if dx == 0:
                    slope = INF
                    intercept = x1
                else:
                    slope = dy / dx
                    intercept = (y1 * dx - x1 * dy) / dx

                # Normalize -0.0 into +0.0
                if slope == -0.0:
                    slope = 0.0
                if intercept == -0.0:
                    intercept = 0.0

                # Midpoint key (unique encoding)
                midPointKey = (x1 + x2) * 10000 + (y1 + y2)

                slopeIntercpts[slope].append(intercept)
                midPointMap[midPointKey].append(slope)

        # Count pairs having same slope but different intercept → parallel lines
        for interceptList in slopeIntercpts.values():
            if len(interceptList) <= 1:
                continue

            freq = {}
            for b in interceptList:
                freq[b] = freq.get(b, 0) + 1

            prefix = 0
            for b in sorted(freq):
                count = freq[b]
                result += prefix * count
                prefix += count

        # Subtract parallelograms via midpoint slope pairs
        for slopeList in midPointMap.values():
            if len(slopeList) <= 1:
                continue

            freq = {}
            for s in slopeList:
                freq[s] = freq.get(s, 0) + 1

            prefix = 0
            for s in sorted(freq):
                count = freq[s]
                result -= prefix * count
                prefix += count

        return result
