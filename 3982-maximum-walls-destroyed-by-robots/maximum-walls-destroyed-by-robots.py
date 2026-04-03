from bisect import bisect_left
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        self.n = len(robots)
        
        # combine robots + distance
        self.arr = [[robots[i], distance[i]] for i in range(self.n)]
        self.arr.sort()  # sort by robot position
        
        self.walls = sorted(walls)
        
        # dp[i][j]
        self.dp = [[None] * 2 for _ in range(self.n)]
        
        return self.dfs(self.n - 1, 1)
    
    def dfs(self, i, j):
        if i < 0:
            return 0
        
        if self.dp[i][j] is not None:
            return self.dp[i][j]
        
        # LEFT OPTION
        left = self.arr[i][0] - self.arr[i][1]
        if i > 0:
            left = max(left, self.arr[i - 1][0] + 1)
        
        l = bisect_left(self.walls, left)
        r = bisect_left(self.walls, self.arr[i][0] + 1)
        
        ans = self.dfs(i - 1, 0) + (r - l)
        
        # RIGHT OPTION
        right = self.arr[i][0] + self.arr[i][1]
        
        if i + 1 < self.n:
            if j == 0:
                right = min(right, self.arr[i + 1][0] - self.arr[i + 1][1] - 1)
            else:
                right = min(right, self.arr[i + 1][0] - 1)
        
        l = bisect_left(self.walls, self.arr[i][0])
        r = bisect_left(self.walls, right + 1)
        
        ans = max(ans, self.dfs(i - 1, 1) + (r - l))
        
        self.dp[i][j] = ans
        return ans