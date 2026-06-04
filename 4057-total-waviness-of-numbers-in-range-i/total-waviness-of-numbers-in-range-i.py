class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0

        for num in range(num1, num2 + 1):
            total += self.get_waviness(num)

        return total

    
    def get_waviness(self, num: int) -> int:
        num_str = str(num)

        if len(num_str) < 3:
            return 0

        waviness = 0

        for i in range(1, len(num_str) - 1):
            current = int(num_str[i])
            left = int(num_str[i - 1])
            right = int(num_str[i + 1])


            # Check if it's a peak
            if current > left and current > right:
                waviness += 1
            # Check if it's a valley
            elif current < left and current < right:
                waviness += 1

        return waviness