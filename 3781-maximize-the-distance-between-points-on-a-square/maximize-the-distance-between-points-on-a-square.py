from typing import List
import bisect

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Step 1: map to perimeter
        perim = []
        for x, y in points:
            if x == 0:
                perim.append(y)
            elif y == side:
                perim.append(side + x)
            elif x == side:
                perim.append(2*side + (side - y))
            else:
                perim.append(3*side + (side - x))
        
        perim.sort()
        P = 4 * side
        n = len(perim)

        extended = perim + [p + P for p in perim]

        def can(d):
            for i in range(n):
                count = 1
                curr = i

                for _ in range(k - 1):
                    target = extended[curr] + d
                    nxt = bisect.bisect_left(extended, target)

                    if nxt >= i + n:
                        break
                    
                    curr = nxt
                    count += 1

                if count >= k:
                    # check circular condition
                    if extended[i] + P - extended[curr] >= d:
                        return True

            return False

        lo, hi = 0, 2 * side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        
        return lo