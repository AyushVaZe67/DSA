from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Store all prefixes from arr1
        prefixes = set()
        
        # For each number in arr1, generate all its prefixes
        for num in arr1:
            # Convert to string to easily get prefixes
            num_str = str(num)
            # Generate all prefixes of this number
            for i in range(1, len(num_str) + 1):
                prefixes.add(num_str[:i])
        
        # Find the longest common prefix
        max_length = 0
        
        # For each number in arr2, check all its prefixes
        for num in arr2:
            num_str = str(num)
            # Check all prefixes of this number
            for i in range(1, len(num_str) + 1):
                prefix = num_str[:i]
                # If this prefix exists in our set from arr1
                if prefix in prefixes:
                    # Update max_length if current prefix is longer
                    max_length = max(max_length, i)
        
        return max_length