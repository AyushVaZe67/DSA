from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # We'll use a difference array to track cost changes
        diff = [0] * (2 * limit + 3)  # Sum can range from 2 to 2*limit
        
        # Process each pair
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            
            # Current sum
            current_sum = a + b
            
            # Range for 1 move: [min(a,b) + 1, max(a,b) + limit]
            lower = min(a, b) + 1
            upper = max(a, b) + limit
            
            # Mark changes in cost
            # Starting at 2, we'll adjust as S increases
            diff[2] += 2  # Initial cost is 2
            
            # Cost becomes 1 in the range [lower, upper]
            diff[lower] -= 1
            diff[upper + 1] += 1
            
            # Cost becomes 0 at current_sum (but only if within range)
            diff[current_sum] -= 1
            diff[current_sum + 1] += 1
        
        # Calculate prefix sum to get cost for each S
        min_moves = float('inf')
        current_cost = 0
        
        for s in range(2, 2 * limit + 1):
            current_cost += diff[s]
            min_moves = min(min_moves, current_cost)
        
        return min_moves