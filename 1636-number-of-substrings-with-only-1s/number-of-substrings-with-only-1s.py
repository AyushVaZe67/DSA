class Solution:
    def numSub(self, s: str) -> int:
        MOD =  10**9 + 7
        total = 0 
        count = 0

        for ch in s:
            if ch == '1':
                count += 1
            else:
                total = (total + count * (count + 1) // 2) % MOD
                count = 0
        
        total = (total + count * (count +1) // 2) % MOD
    
        return total