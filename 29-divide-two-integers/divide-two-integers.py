class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow case: -2^31 / -1 = 2^31 which exceeds 2^31 - 1
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        
        quotient = 0
        
        # Subtract divisor from dividend using bit manipulation
        while dividend_abs >= divisor_abs:
            # Find the largest multiple of divisor that fits in current dividend
            temp = divisor_abs
            multiple = 1
            
            # Double the divisor until it exceeds the dividend
            while dividend_abs >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            # Subtract the largest multiple found
            dividend_abs -= temp
            quotient += multiple
        
        # Apply the sign
        if negative:
            quotient = -quotient
        
        # Ensure result is within 32-bit signed integer range
        return max(-2**31, min(2**31 - 1, quotient))