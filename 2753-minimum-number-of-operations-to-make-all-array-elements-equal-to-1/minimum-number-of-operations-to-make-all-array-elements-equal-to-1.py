class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        overall_gcd = 0
        for num in nums:
            overall_gcd = gcd(overall_gcd, num)
        if overall_gcd != 1:
            return -1

        ones = nums.count(1)
        if ones > 0:
            return n - ones


        min_len = float('inf')
        for i in range(n):
            curr_gcd = nums[i]
            if curr_gcd == 1:
                min_len = 1
                break
            for j in range(i+1,n):
                curr_gcd = gcd(curr_gcd, nums[j])
                if curr_gcd == 1:
                    min_len = min(min_len, j-i+1)
                    break

        return (min_len - 1) + (n - 1)