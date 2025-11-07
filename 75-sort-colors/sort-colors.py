class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap with low pointer and move both forward
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Just move mid forward (1s are in the right place)
                mid += 1
            else:  # nums[mid] == 2
                # Swap with high pointer and move high backward
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1