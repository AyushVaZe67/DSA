class Solution:
    def minimumDistance(self, word: str) -> int:
        # Mapping: alphabetical order with 6 columns per row
        def get_coord(c):
            idx = ord(c) - ord('A')
            row = idx // 6
            col = idx % 6
            return (row, col)
        
        n = len(word)
        if n <= 1:
            return 0
        
        pos = [get_coord(c) for c in word]
        
        # dp[i][j] = min distance after typing i+1 characters
        # where one finger is at pos[i] (last typed), other at pos[j] (j < i)
        # j can be -1 meaning other finger not placed yet
        INF = 10**9
        dp = [[INF] * (n + 1) for _ in range(n)]
        
        # First character: one finger at pos[0], other not placed
        dp[0][n] = 0  # Use n to represent -1 (other finger not placed)
        
        for i in range(1, n):
            for j in range(n + 1):
                if dp[i-1][j] == INF:
                    continue
                
                # Get position of other finger
                other_pos = None if j == n else pos[j]
                last_pos = pos[i-1]
                curr_pos = pos[i]
                
                # Option 1: Use last finger to type current character
                dist_last = abs(last_pos[0] - curr_pos[0]) + abs(last_pos[1] - curr_pos[1])
                dp[i][j] = min(dp[i][j], dp[i-1][j] + dist_last)
                
                # Option 2: Use other finger to type current character
                if other_pos is not None:
                    dist_other = abs(other_pos[0] - curr_pos[0]) + abs(other_pos[1] - curr_pos[1])
                    dp[i][i-1] = min(dp[i][i-1], dp[i-1][j] + dist_other)
                else:
                    # Other finger not placed yet, placing it now costs 0
                    dp[i][i-1] = min(dp[i][i-1], dp[i-1][j])
        
        # Find minimum distance after typing all characters
        result = INF
        for j in range(n + 1):
            result = min(result, dp[n-1][j])
        
        return result