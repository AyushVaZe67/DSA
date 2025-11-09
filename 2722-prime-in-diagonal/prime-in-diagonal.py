class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        diagonal_elements = set()

        for i in range(n):
            diagonal_elements.add(nums[i][i])
            diagonal_elements.add(nums[i][n - i - 1])

        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False        
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        largest = 0
        for val in diagonal_elements:
            if is_prime(val) and val > largest:
                largest = val
        
        return largest