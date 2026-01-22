from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # Make a copy to work with
        arr = nums[:]
        operations = 0
        
        # Helper to check if array is non-decreasing
        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True
        
        # Continue until array is non-decreasing
        while not is_sorted(arr):
            # Find adjacent pair with minimum sum (leftmost if tie)
            min_sum = float('inf')
            min_index = -1
            
            for i in range(len(arr) - 1):
                pair_sum = arr[i] + arr[i+1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_index = i
            
            # Merge at min_index
            arr[min_index] = min_sum
            # Remove the element at min_index + 1
            arr.pop(min_index + 1)
            
            operations += 1
        
        return operations