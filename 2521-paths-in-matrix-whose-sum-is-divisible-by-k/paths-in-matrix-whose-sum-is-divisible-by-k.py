class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        m ,n = len(grid), len(grid[0])

        dp = [[0] * k for _ in range(n)]

        dp[0][grid[0][0] % k] = 1

        for i in range(m):
            new_dp = [[0] * k for _ in range(n)]
            for j in range(n):
                val = grid[i][j] % k

                if i == 0 and j == 0:
                    new_dp[0][val] = 1
                    continue

                if i > 0:
                    prev = dp[j]
                    if any(prev):
                        for r in range(k):
                            cnt = prev[r]
                            if cnt:
                                new_r = (r+val) % k
                                new_dp[j][new_r] = (new_dp[j][new_r] + cnt) % MOD

                if j > 0:
                    left = new_dp[j-1]
                    if any(left):
                        for r in range(k):
                            cnt = left[r]
                            if cnt:
                                new_r = (r+val) % k
                                new_dp[j][new_r] = (new_dp[j][new_r] + cnt) % MOD

            dp = new_dp

        return dp[n-1][0] % MOD            
        