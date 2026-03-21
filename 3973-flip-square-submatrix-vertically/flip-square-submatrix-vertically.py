class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        result = [row[:] for row in grid]

        for i in range(k):
            result[x + i][y:y + k] = grid[x + k - 1 - i][y:y + k]
        return result