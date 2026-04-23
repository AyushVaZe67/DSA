from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Group indices by their values
        value_to_indices = defaultdict(list)
        for i, num in enumerate(nums):
            value_to_indices[num].append(i)
        
        # Initialize result array with zeros
        result = [0] * len(nums)
        
        # Process each group of indices
        for indices in value_to_indices.values():
            n = len(indices)
            if n == 1:
                continue
            
            # Calculate prefix sums for this group
            prefix_sum = [0] * (n + 1)
            for i in range(n):
                prefix_sum[i + 1] = prefix_sum[i] + indices[i]
            
            # For each index in the group, calculate sum of distances
            for i in range(n):
                # Left side: indices[i] - each index on the left
                left_count = i
                left_sum = left_count * indices[i] - prefix_sum[i]
                
                # Right side: each index on the right - indices[i] 
                right_count = n - i - 1
                right_sum = (prefix_sum[n] - prefix_sum[i + 1]) - right_count * indices[i]
                
                result[indices[i]] = left_sum + right_sum
        
        return result