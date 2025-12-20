class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # If there's only 1 row, all columns are automatically sorted
        if len(strs) <= 1:
            return 0
        
        rows = len(strs)
        cols = len(strs[0])
        delete_count = 0
        
        # Check each column
        for col in range(cols):
            # Check if this column is sorted
            for row in range(1, rows):
                # If we find a character that's smaller than the previous one
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break
        
        return delete_count