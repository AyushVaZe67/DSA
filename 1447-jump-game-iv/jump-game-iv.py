from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        # Build mapping of value to all indices with that value
        value_to_indices = defaultdict(list)
        for i, val in enumerate(arr):
            value_to_indices[val].append(i)
        
        # BFS setup
        visited = set([0])
        queue = deque([(0, 0)])  # (index, steps)
        
        while queue:
            index, steps = queue.popleft()
            
            # If we reached the last index
            if index == n - 1:
                return steps
            
            # Try jumping to same-valued indices
            if arr[index] in value_to_indices:
                for neighbor in value_to_indices[arr[index]]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
                # Important optimization: remove this value to avoid reprocessing
                del value_to_indices[arr[index]]
            
            # Try adjacent jumps
            for neighbor in [index - 1, index + 1]:
                if 0 <= neighbor < n and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        return -1  # Should never reach here as array is connected