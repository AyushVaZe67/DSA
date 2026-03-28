from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        
        # Check diagonal property
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
        
        # Check symmetry and bounds
        for i in range(n):
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                if lcp[i][j] > n - i or lcp[i][j] > n - j:
                    return ""
        
        # Build the string
        result = [''] * n
        current_char = 0
        
        for i in range(n):
            if result[i] != '':
                continue
            
            # Assign new character
            if current_char >= 26:
                return ""
            result[i] = chr(ord('a') + current_char)
            current_char += 1
            
            # Mark positions that must have the same character
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    if result[j] == '':
                        result[j] = result[i]
                    elif result[j] != result[i]:
                        return ""
        
        # Verify the constructed string using the LCP property
        # Create a verification matrix
        verify_lcp = [[0] * n for _ in range(n)]
        
        # Fill from bottom-right to top-left using DP
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if result[i] == result[j]:
                    if i == n-1 or j == n-1:
                        verify_lcp[i][j] = 1
                    else:
                        verify_lcp[i][j] = verify_lcp[i+1][j+1] + 1
                else:
                    verify_lcp[i][j] = 0
        
        # Compare with given lcp
        for i in range(n):
            for j in range(n):
                if verify_lcp[i][j] != lcp[i][j]:
                    return ""
        
        return ''.join(result)