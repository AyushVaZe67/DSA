class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ''
        for i in range(len(digits)):
            temp = temp + str(digits[i])
            temp1 = int(temp) + 1
        return list(map(int, str(temp1)))