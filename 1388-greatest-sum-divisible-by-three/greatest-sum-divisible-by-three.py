class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        NEG = -10**18
        dp = [0, NEG, NEG]

        for num in nums:
            tmp = dp[:]
            for r in range(3):
                new_r = (r + num) % 3
                tmp[new_r] = max(tmp[new_r], dp[r] + num)
            dp = tmp

        return dp[0]
