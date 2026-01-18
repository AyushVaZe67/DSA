from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Row prefix sums
        rowPref = [[0]*(n+1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                rowPref[i][j+1] = rowPref[i][j] + grid[i][j]
        
        # Column prefix sums
        colPref = [[0]*(m+1) for _ in range(n)]
        for j in range(n):
            for i in range(m):
                colPref[j][i+1] = colPref[j][i] + grid[i][j]
        
        def getRowSum(r, c1, c2):
            return rowPref[r][c2+1] - rowPref[r][c1]
        
        def getColSum(c, r1, r2):
            return colPref[c][r2+1] - colPref[c][r1]
        
        def isMagic(r, c, k):
            # First row sum as target
            target = getRowSum(r, c, c+k-1)
            
            # Check rows
            for i in range(r, r+k):
                if getRowSum(i, c, c+k-1) != target:
                    return False
            
            # Check columns
            for j in range(c, c+k):
                if getColSum(j, r, r+k-1) != target:
                    return False
            
            # Main diagonal
            diag_sum = 0
            for d in range(k):
                diag_sum += grid[r+d][c+d]
            if diag_sum != target:
                return False
            
            # Anti-diagonal
            anti_diag_sum = 0
            for d in range(k):
                anti_diag_sum += grid[r+d][c+k-1-d]
            if anti_diag_sum != target:
                return False
            
            return True
        
        # Try from largest k to smallest
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if isMagic(r, c, k):
                        return k
        return 1