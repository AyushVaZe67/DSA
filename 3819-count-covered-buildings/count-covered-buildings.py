class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)
        
        for x in rows:
            rows[x].sort()
        for y in cols:
            cols[y].sort()
        
        building_set = set(tuple(b) for b in buildings)
        count = 0
        
        for x, y in buildings:
            y_list = rows[x]
            idx = bisect.bisect_left(y_list, y)
            left = False
            if idx > 0:
                left = True
            
            right = False
            if idx < len(y_list) - 1:
                right = True
            
            x_list = cols[y]
            idx = bisect.bisect_left(x_list, x)
            above = False
            if idx > 0:
                above = True
            
            below = False
            if idx < len(x_list) - 1:
                below = True
            
            if left and right and above and below:
                count += 1
        
        return count