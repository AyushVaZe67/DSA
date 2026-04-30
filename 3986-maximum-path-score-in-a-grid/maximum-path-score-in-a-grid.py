from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # DP table: each cell contains a dict mapping cost to max score
        dp = [[{} for _ in range(n)] for _ in range(m)]
        
        # Start at top-left corner
        start_val = grid[0][0]
        start_cost = 0 if start_val == 0 else 1
        start_score = start_val if start_val > 0 else 0
        
        if start_cost <= k:
            dp[0][0][start_cost] = start_score
        
        # Fill DP table
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                current_val = grid[i][j]
                current_cost_add = 0 if current_val == 0 else 1
                current_score_add = current_val if current_val > 0 else 0
                
                # Reachable from above
                if i > 0:
                    for cost, score in dp[i-1][j].items():
                        new_cost = cost + current_cost_add
                        if new_cost <= k:
                            new_score = score + current_score_add
                            if new_cost not in dp[i][j] or dp[i][j][new_cost] < new_score:
                                dp[i][j][new_cost] = new_score
                
                # Reachable from left
                if j > 0:
                    for cost, score in dp[i][j-1].items():
                        new_cost = cost + current_cost_add
                        if new_cost <= k:
                            new_score = score + current_score_add
                            if new_cost not in dp[i][j] or dp[i][j][new_cost] < new_score:
                                dp[i][j][new_cost] = new_score
                
                # Prune dominated states for current cell
                # Keep only states where no other state has higher score with same or lower cost
                if dp[i][j]:
                    states = sorted(dp[i][j].items())  # Sort by cost
                    pruned = {}
                    max_score_so_far = -1
                    for cost, score in states:
                        if score > max_score_so_far:
                            max_score_so_far = score
                            pruned[cost] = score
                    dp[i][j] = pruned
        
        # Check if we can reach bottom-right
        if not dp[m-1][n-1]:
            return -1
        
        # Return maximum score from bottom-right cell
        return max(dp[m-1][n-1].values())