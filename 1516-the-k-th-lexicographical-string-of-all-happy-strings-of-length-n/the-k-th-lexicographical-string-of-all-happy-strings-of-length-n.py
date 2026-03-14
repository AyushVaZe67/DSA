class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def count_strings(remaining, last_char):
            if remaining == 0:
                return 1
            
            total = 0
            for c in ['a', 'b', 'c']:
                if c != last_char:
                    total += count_strings(remaining - 1, c)
            
            return total
        
        result = []
        remaining = n
        last_char = ''  
        
        while remaining > 0:
            for c in ['a', 'b', 'c']:
                if c == last_char:
                    continue
                
                count = count_strings(remaining - 1, c)
                e
                if count >= k:
                    result.append(c)
                    last_char = c
                    remaining -= 1
                    break
                else:
                    k -= count
            else:
                return ''
        
        return ''.join(result)