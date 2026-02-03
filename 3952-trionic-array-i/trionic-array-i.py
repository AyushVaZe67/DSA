from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False
        
        prefix_inc = [True] * n
        for i in range(1, n):
            prefix_inc[i] = prefix_inc[i-1] and (nums[i-1] < nums[i])
        
        suffix_inc = [True] * n
        for i in range(n-2, -1, -1):
            suffix_inc[i] = (nums[i] < nums[i+1]) and suffix_inc[i+1]
        
        for p in range(1, n-1):
            if not prefix_inc[p]:
                continue
            for q in range(p+1, n-1):
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