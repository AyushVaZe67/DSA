from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # Initialize DP array with negative infinity
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Starting point
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            # We can neutralize the starting cell
            dp[0][0][1] = 0
        
        # Fill DP table
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] == -float('inf'):
                        continue
                    
                    # Try moving right
                    if j + 1 < n:
                        # Option 1: Don't neutralize the new cell
                        new_val = dp[i][j][k] + coins[i][j+1]
                        dp[i][j+1][k] = max(dp[i][j+1][k], new_val)
                        
                        # Option 2: Neutralize the new cell if it's negative and we have neutralizations left
                        if coins[i][j+1] < 0 and k < 2:
                            new_val = dp[i][j][k]  # No coin lost from negative cell
                            dp[i][j+1][k+1] = max(dp[i][j+1][k+1], new_val)
                    
                    # Try moving down
                    if i + 1 < m:
                        # Option 1: Don't neutralize the new cell
                        new_val = dp[i][j][k] + coins[i+1][j]
                        dp[i+1][j][k] = max(dp[i+1][j][k], new_val)
                        
                        # Option 2: Neutralize the new cell if it's negative and we have neutralizations left
                        if coins[i+1][j] < 0 and k < 2:
                            new_val = dp[i][j][k]  # No coin lost from negative cell
                            dp[i+1][j][k+1] = max(dp[i+1][j][k+1], new_val)
        
        # Return the maximum value at the destination using any number of neutralizations (0, 1, or 2)
        return max(dp[m-1][n-1][0], dp[m-1][n-1][1], dp[m-1][n-1][2])