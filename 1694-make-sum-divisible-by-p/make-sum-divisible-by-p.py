class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        total_mod = total_sum % p

        if total_mod == 0:
            return 0

        target_rem = total_mod
        prefix_mod = 0
        n = len(nums)
        min_len = n

        last_occurence = {0: -1}

        for j in range(n):
            prefix_mod = (prefix_mod + nums[j]) % p
            need = (prefix_mod - target_rem) % p
            if need < 0:
                need += p

            if need in last_occurence:
                length = j - last_occurence[need]
                if length != n:
                    min_len = min(min_len, length)

            last_occurence[prefix_mod] = j

        return min_len if min_len != n else -1
            