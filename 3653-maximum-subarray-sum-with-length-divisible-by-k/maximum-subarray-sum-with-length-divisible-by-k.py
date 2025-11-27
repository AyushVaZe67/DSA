class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]


        min_prefix = [float('inf')] * k
        min_prefix[0] = prefix[0]

        max_sum = -float('inf')

        for i in range(1,n+1):
            residue = i % k
        
            if i >= k:
                max_sum = max(max_sum, prefix[i] - min_prefix[residue])

            min_prefix[residue] = min(min_prefix[residue], prefix[i])

        return max_sum
        