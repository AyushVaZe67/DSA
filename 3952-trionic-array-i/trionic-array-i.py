from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False
        
        # prefix_inc[i]: nums[0..i] strictly increasing
        prefix_inc = [True] * n
        for i in range(1, n):
            prefix_inc[i] = prefix_inc[i-1] and (nums[i-1] < nums[i])
        
        # suffix_inc[i]: nums[i..n-1] strictly increasing
        suffix_inc = [True] * n
        for i in range(n-2, -1, -1):
            suffix_inc[i] = (nums[i] < nums[i+1]) and suffix_inc[i+1]
        
        # Check all valid p, q
        for p in range(1, n-1):
            if not prefix_inc[p]:
                continue
            # Try all possible q
            for q in range(p+1, n-1):
                # Check decreasing from p to q
                dec_ok = True
                for i in range(p, q):
                    if nums[i] <= nums[i+1]:
                        dec_ok = False
                        break
                if not dec_ok:
                    continue
                if suffix_inc[q]:
                    return True
        return False