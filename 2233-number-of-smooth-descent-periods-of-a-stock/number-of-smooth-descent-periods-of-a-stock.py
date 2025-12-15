class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        total_periods = 0
        current_length = 1

        for i in range(1, n):
            if prices[i] == prices[i-1] - 1:
                current_length += 1
            else:
                total_periods += current_length * (current_length + 1) // 2
                current_length = 1

        total_periods += current_length * (current_length + 1) // 2

        return total_periods 