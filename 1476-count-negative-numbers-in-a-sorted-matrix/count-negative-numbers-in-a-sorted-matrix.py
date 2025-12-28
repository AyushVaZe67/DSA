class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row, col, count = 0, cols -1, 0

        while row < rows and col >= 0:
            if grid[row][col] < 0:
                count += rows - row
                col -= 1
            else:
                row += 1
        
        return count