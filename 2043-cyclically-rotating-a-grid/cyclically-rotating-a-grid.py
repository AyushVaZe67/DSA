from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        
        for layer in range(num_layers):
            # Extract the current layer
            elements = []
            
            # Top row (left to right)
            for j in range(layer, n - layer):
                elements.append(grid[layer][j])
            
            # Right column (top to bottom, excluding top element)
            for i in range(layer + 1, m - layer):
                elements.append(grid[i][n - 1 - layer])
            
            # Bottom row (right to left, excluding right element)
            for j in range(n - 2 - layer, layer - 1, -1):
                elements.append(grid[m - 1 - layer][j])
            
            # Left column (bottom to top, excluding bottom and top elements)
            for i in range(m - 2 - layer, layer, -1):
                elements.append(grid[i][layer])
            
            # Rotate the elements by k positions counter-clockwise
            # Since we want counter-clockwise rotation, we shift the list by k
            if elements:
                k_effective = k % len(elements)
                rotated = elements[k_effective:] + elements[:k_effective]
            
            # Put elements back in the same order
            idx = 0
            
            # Top row
            for j in range(layer, n - layer):
                grid[layer][j] = rotated[idx]
                idx += 1
            
            # Right column
            for i in range(layer + 1, m - layer):
                grid[i][n - 1 - layer] = rotated[idx]
                idx += 1
            
            # Bottom row
            for j in range(n - 2 - layer, layer - 1, -1):
                grid[m - 1 - layer][j] = rotated[idx]
                idx += 1
            
            # Left column
            for i in range(m - 2 - layer, layer, -1):
                grid[i][layer] = rotated[idx]
                idx += 1
        
        return grid