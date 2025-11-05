class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31      # -2147483648
        INT_MAX = 2**31 - 1   # 2147483647

        str_x = str(x)
        if str_x[0] == '-':
            str_new = str_x[1:]
            rev_str = str_new[::-1]
            result = -int(rev_str)
        else:
            str_new = str_x
            rev_str = str_new[::-1]
            result = int(rev_str)
        
        # Check for overflow after conversion
        if result < INT_MIN or result > INT_MAX:
            return 0
        
        return result