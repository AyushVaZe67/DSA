class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operation = 0
        for num in nums:
            remainder = num % 3
            operation += min(remainder, 3 - remainder)
        return operation