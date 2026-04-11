from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Group indices by value
        indices_map = defaultdict(list)
        for i, num in enumerate(nums):
            indices_map[num].append(i)
        
        min_distance = float('inf')
        
        # For each value that appears at least 3 times
        for indices in indices_map.values():
            if len(indices) < 3:
                continue
            
            # Check all consecutive triplets (this is optimal)
            for j in range(2, len(indices)):
                i = j - 2
                k = j
                # indices[i] < indices[i+1] < indices[j] < indices[k]
                distance = 2 * (indices[k] - indices[i])
                min_distance = min(min_distance, distance)
        
        return min_distance if min_distance != float('inf') else -1