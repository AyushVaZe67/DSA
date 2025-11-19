class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        found = True

        while found:
            found = False
            for num in nums:
                if num == original:
                    original = 2 * original
                    found = True
                    break

        return original
            
        
        