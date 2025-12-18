from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        m = k // 2
        
        # Original profit
        original = 0
        for i in range(n):
            original += strategy[i] * prices[i]
        
        # Precompute A and B
        A = [-strategy[i] * prices[i] for i in range(n)]
        B = [prices[i] * (1 - strategy[i]) for i in range(n)]
        
        max_delta = 0
        
        # First window sums
        if n >= k:
            sumA = sum(A[0:m])
            sumB = sum(B[m:k])
            max_delta = max(max_delta, sumA + sumB)
            
            # Sliding window
            for L in range(1, n - k + 1):
                sumA = sumA - A[L-1] + A[L+m-1]
                sumB = sumB - B[L+m-1] + B[L+k-1]
                delta = sumA + sumB
                if delta > max_delta:
                    max_delta = delta
        
        return original + max_delta