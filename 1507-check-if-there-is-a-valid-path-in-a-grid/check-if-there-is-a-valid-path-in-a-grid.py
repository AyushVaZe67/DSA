from typing import List
from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Define connection directions for each street type
        # For each direction [up, right, down, left] where 4 directions = [(-1,0), (0,1), (1,0), (0,-1)]
        # 1 means connected in that direction, 0 means not connected
        street_connections = {
            1: [0, 1, 0, 1],  # left-right: up(0), right(1), down(0), left(1)
            2: [1, 0, 1, 0],  # up-down: up(1), right(0), down(1), left(0)
            3: [0, 0, 1, 1],  # left-down: up(0), right(0), down(1), left(1)
            4: [0, 1, 1, 0],  # right-down: up(0), right(1), down(1), left(0)
            5: [1, 0, 0, 1],  # left-up: up(1), right(0), down(0), left(1)
            6: [1, 1, 0, 0]   # right-up: up(1), right(1), down(0), left(0)
        }
        
        # Directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # Opposite direction indices: opposite of up(0) is down(2), right(1) is left(3), etc.
        opposite = {0: 2, 1: 3, 2: 0, 3: 1}
        
        # BFS
        visited = [[False] * n for _ in range(m)]
        queue = deque()
        queue.append((0, 0))
        visited[0][0] = True
        
        while queue:
            x, y = queue.popleft()
            
            # If reached destination
            if x == m - 1 and y == n - 1:
                return True
            
            current_street = grid[x][y]
            
            # Check all 4 directions
            for dir_idx, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                
                # Check boundaries
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                
                if visited[nx][ny]:
                    continue
                
                # Check if current cell has connection in this direction
                if street_connections[current_street][dir_idx] == 0:
                    continue
                
                # Check if neighbor cell has connection from the opposite direction
                neighbor_street = grid[nx][ny]
                opposite_dir_idx = opposite[dir_idx]
                
                if street_connections[neighbor_street][opposite_dir_idx] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        
        return False