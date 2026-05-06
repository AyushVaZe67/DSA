from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        
        # Rotate 90° clockwise
        rotated = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = boxGrid[i][j]
        
        # Apply gravity to each column in rotated box
        for col in range(m):
            # Position where next stone can fall
            empty_spot = n - 1
            # Go from bottom to top
            for row in range(n - 1, -1, -1):
                if rotated[row][col] == '*':
                    # Obstacle blocks further falling
                    empty_spot = row - 1
                elif rotated[row][col] == '#':
                    # Move stone to empty spot if needed
                    if row != empty_spot:
                        rotated[empty_spot][col] = '#'
                        rotated[row][col] = '.'
                    empty_spot -= 1
        
        return rotated