class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for optimization
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # Corrected: +1 to handle both even and odd cases
        
        # Binary search on the smaller array
        left, right = 0, m
        
        while left <= right:
            # Partition nums1
            i = (left + right) // 2  # elements from nums1 in left partition
            j = half - i             # elements from nums2 in left partition
            
            # Handle edge cases for boundaries
            nums1_left = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right = float('inf') if i == m else nums1[i]
            nums2_left = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right = float('inf') if j == n else nums2[j]
            
            # Check if we found the correct partition
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Found the correct partition
                if total % 2 == 1:  # Odd total length
                    return max(nums1_left, nums2_left)  # Corrected: max of left partition
                else:  # Even total length
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                # Too many elements from nums1 in left partition
                right = i - 1
            else:
                # Too few elements from nums1 in left partition
                left = i + 1
        
        return 0.0