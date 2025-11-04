class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        rev_str = x_str[::-1]  # reverse the string
        if x_str == rev_str:
            return True
        else:
            return False
