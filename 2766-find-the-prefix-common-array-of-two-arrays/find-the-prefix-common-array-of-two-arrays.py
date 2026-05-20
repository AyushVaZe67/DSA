from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n + 1)  # Track how many times we've seen each number
        result = []
        common_count = 0
        
        for i in range(n):
            # Process A[i]
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common_count += 1
            
            # Process B[i]
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common_count += 1
            
            result.append(common_count)
        
        return result