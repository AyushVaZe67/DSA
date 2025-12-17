from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        INF = 10**9
        # dp[t][i][state]: state 0=neutral, 1=long, 2=short
        dp = [[[-INF] * 3 for _ in range(n)] for _ in range(k+1)]
        
        # Initialize at day 0
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]  # open long on day 0
        dp[0][0][2] = prices[0]   # open short on day 0
        
        for t in range(k+1):
            for i in range(1, n):
                # Stay neutral
                dp[t][i][0] = max(dp[t][i][0], dp[t][i-1][0])
                
                # From neutral, open long
                dp[t][i][1] = max(dp[t][i-1][1], dp[t][i-1][0] - prices[i])
                
                # From neutral, open short
                dp[t][i][2] = max(dp[t][i-1][2], dp[t][i-1][0] + prices[i])
                
                # From long, close (sell) to complete a transaction
                if t > 0:
                    dp[t][i][0] = max(dp[t][i][0], dp[t-1][i-1][1] + prices[i])
                
                # From short, close (buy back) to complete a transaction  
                if t > 0:
                    dp[t][i][0] = max(dp[t][i][0], dp[t-1][i-1][2] - prices[i])
                
                # Also track staying in positions from previous day
                dp[t][i][1] = max(dp[t][i][1], dp[t][i-1][1])
                dp[t][i][2] = max(dp[t][i][2], dp[t][i-1][2])
        
        # Answer is max of dp[t][n-1][0] for all t
        return max(dp[t][n-1][0] for t in range(k+1))