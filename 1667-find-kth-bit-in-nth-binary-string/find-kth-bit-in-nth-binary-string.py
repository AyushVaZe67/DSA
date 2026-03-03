class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        length = 2**n - 1
        mid = length // 2 + 1

        if k == mid:
            return '1'
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            mirrored_k = mid - (k - mid)
            result = self.findKthBit(n - 1, mirrored_k)
            return '0' if result == '1' else '1'
            
        