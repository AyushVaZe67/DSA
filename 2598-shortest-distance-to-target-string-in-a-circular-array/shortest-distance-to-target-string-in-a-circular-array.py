from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_distance = float('inf')
        
        # Check each index for the target
        for i in range(n):
            if words[i] == target:
                # Calculate distance going forward
                forward_dist = (i - startIndex + n) % n
                # Calculate distance going backward
                backward_dist = (startIndex - i + n) % n
                # Take the minimum of the two directions
                distance = min(forward_dist, backward_dist)
                # Update global minimum
                min_distance = min(min_distance, distance)
        
        return -1 if min_distance == float('inf') else min_distance