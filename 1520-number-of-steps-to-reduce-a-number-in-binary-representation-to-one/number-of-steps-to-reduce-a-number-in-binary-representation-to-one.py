class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        # Convert to list for easier manipulation
        bits = list(s)
        
        # Continue until we reach "1"
        while len(bits) > 1 or bits[0] != '1':
            if bits[-1] == '0':  # Even - divide by 2
                bits.pop()
            else:  # Odd - add 1
                # Add 1 to binary number
                i = len(bits) - 1
                while i >= 0 and bits[i] == '1':
                    bits[i] = '0'
                    i -= 1
                
                if i >= 0:
                    bits[i] = '1'
                else:
                    # All digits were 1, need to prepend 1
                    bits.insert(0, '1')
            
            steps += 1
        
        return steps