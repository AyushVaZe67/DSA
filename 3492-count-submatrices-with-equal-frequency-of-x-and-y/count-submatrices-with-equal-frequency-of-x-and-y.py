class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0 

        rows, cols = len(grid), len(grid[0])

        prefix_x = [[0] * (cols + 1) for _ in range(rows + 1)]
        prefix_y = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                prefix_x[i + 1][j + 1] = prefix_x[i][j + 1] + prefix_x[i + 1][j] - prefix_x[i][j]
                prefix_y[i + 1][j + 1] = prefix_y[i][j + 1] + prefix_y[i + 1][j] - prefix_y[i][j]

                if grid[i][j] == 'X':
                    prefix_x[i+1][j+1] += 1
                elif grid[i][j] == 'Y':
                    prefix_y[i+1][j+1] += 1
                

        count = 0

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                x_count = prefix_x[i][j]
                y_count = prefix_y[i][j]

                if x_count > 0 and x_count == y_count:
                    count += 1
        
        return count
        