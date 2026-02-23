class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        seen = set()
        total_codes = 1 << k

        for i in range(len(s) - k + 1):
            val = int(s[i:i+k], 2)
            seen.add(val)

            if len(seen) == total_codes:
                return True
        
        return len(seen) == total_codes
        