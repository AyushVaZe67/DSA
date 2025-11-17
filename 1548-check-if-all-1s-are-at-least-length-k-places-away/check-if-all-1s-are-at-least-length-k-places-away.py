class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_index = -k - 1

        for i,num in enumerate(nums):
            if num == 1:
                if i - last_one_index <= k:
                    return False
                last_one_index = i
        return True