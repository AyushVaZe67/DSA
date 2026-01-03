class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        aba, abc = 6, 6
        for _ in range(1, n):
            new_aba = (3 * aba + 2 * abc) % MOD
            new_abc = (2 * aba + 2 * abc) % MOD
            aba, abc = new_aba, new_abc
        return (aba + abc) % MOD