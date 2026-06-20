from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Add the first building as a restriction (height 0 at position 1)
        restrictions.append([1, 0])
        
        # Sort restrictions by building index
        restrictions.sort()
        
        # If the last restriction isn't at building n, add a dummy restriction
        # This helps with the rightmost boundary
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])  # maximum possible height at n
            
        # First pass: propagate constraints from left to right
        # For each pair of adjacent restrictions, ensure the right one 
        # is reachable from the left one given the slope constraint
        for i in range(1, len(restrictions)):
            prev_idx, prev_h = restrictions[i-1]
            curr_idx, curr_h = restrictions[i]
            # The height at curr_idx cannot exceed prev_h + (curr_idx - prev_idx)
            restrictions[i] = [curr_idx, min(curr_h, prev_h + (curr_idx - prev_idx))]
        
        # Second pass: propagate constraints from right to left
        for i in range(len(restrictions) - 2, -1, -1):
            curr_idx, curr_h = restrictions[i]
            next_idx, next_h = restrictions[i+1]
            # The height at curr_idx cannot exceed next_h + (next_idx - curr_idx)
            restrictions[i] = [curr_idx, min(curr_h, next_h + (next_idx - curr_idx))]
        
        # Now find the maximum possible height
        max_height = 0
        for i in range(len(restrictions) - 1):
            idx1, h1 = restrictions[i]
            idx2, h2 = restrictions[i+1]
            distance = idx2 - idx1
            
            # Between these two restricted buildings, we can go up and then down
            # The maximum height we can achieve is when we go up from h1, 
            # reach a peak, and then go down to h2
            # The peak height = (h1 + h2 + distance) // 2
            peak = (h1 + h2 + distance) // 2
            max_height = max(max_height, peak)
        
        return max_height