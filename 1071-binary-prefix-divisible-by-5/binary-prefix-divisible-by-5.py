class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        current = 0

        for num in nums:
            current = (current * 2 + num) % 5
            result.append(current == 0)

        return result