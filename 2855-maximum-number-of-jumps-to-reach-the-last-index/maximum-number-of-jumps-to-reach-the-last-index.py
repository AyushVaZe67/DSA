from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        # dp[i] = max jumps to reach index i
        dp = [-1] * n
        dp[0] = 0  # 0 jumps to reach start
        
        for i in range(n):
            # If current index is reachable
            if dp[i] >= 0:
                # Try to jump to all future indices
                for j in range(i + 1, n):
                    if abs(nums[j] - nums[i]) <= target:
                        dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[n - 1]