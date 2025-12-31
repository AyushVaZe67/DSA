class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0] * col for _ in  range(row)]
        parent = {}
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        for i in range(row):
            for j in range(col):
                parent[(i,j)] = (i,j)
        
        parent['top'] = 'top'
        parent['bottom'] = 'bottom'

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        def connect(r, c):
            grid[r][c] = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    union((r,c), (nr, nc))

            if r == 0:
                union((r,c), 'top')
            if r == row - 1:
                union((r,c), 'bottom')
        
        for day in range(len(cells)-1,-1,-1):
            r, c = cells[day][0] - 1, cells[day][1] - 1
            connect(r, c)
            if find('top') == find('bottom'):
                return day
    
        return 0