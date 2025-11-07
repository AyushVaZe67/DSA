class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        negative = (dividend < 0) != (divisor < 0)
        
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        
        quotient = 0
        
        while dividend_abs >= divisor_abs:
            temp = divisor_abs
            multiple = 1
            
            while dividend_abs >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend_abs -= temp
            quotient += multiple
        
        if negative:
            quotient = -quotient
        
        return max(-2**31, min(2**31 - 1, quotient))