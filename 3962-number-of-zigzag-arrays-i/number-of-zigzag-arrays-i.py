class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        if n == 1:
            return m % MOD
        if n == 2:
            return (m * (m - 1)) % MOD
        
        # dp0[v] = ways ending with value v (0-indexed), last step down
        # dp1[v] = ways ending with value v, last step up
        dp0 = [0] * m
        dp1 = [0] * m
        
        # length 2
        for v in range(m):
            dp0[v] = m - 1 - v
            dp1[v] = v
        
        # length >= 3
        for _ in range(3, n + 1):
            # Compute suffix sums for dp1 (for dp0_new)
            # and prefix sums for dp0 (for dp1_new)
            suffix1 = 0
            # We'll compute new arrays in place
            new_dp0 = [0] * m
            new_dp1 = [0] * m
            
            # First compute prefix sums for dp0
            prefix0 = 0
            for v in range(m):
                new_dp1[v] = prefix0 % MOD
                prefix0 = (prefix0 + dp0[v]) % MOD
            
            # Then compute suffix sums for dp1
            suffix1 = 0
            for v in range(m-1, -1, -1):
                new_dp0[v] = suffix1 % MOD
                suffix1 = (suffix1 + dp1[v]) % MOD
            
            dp0, dp1 = new_dp0, new_dp1
        
        return (sum(dp0) + sum(dp1)) % MOD