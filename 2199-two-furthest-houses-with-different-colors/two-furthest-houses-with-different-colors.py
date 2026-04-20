from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        
        # Check from the left: find farthest index with different color from colors[0]
        left_max = 0
        for i in range(n-1, -1, -1):
            if colors[i] != colors[0]:
                left_max = i - 0
                break
        
        # Check from the right: find farthest index from the end with different color from colors[-1]
        right_max = 0
        for i in range(n):
            if colors[i] != colors[-1]:
                right_max = (n-1) - i
                break
        
        # Return the maximum distance
        return max(left_max, right_max)