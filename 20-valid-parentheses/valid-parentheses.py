class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Stack to keep track of opening brackets
        stack = []
        
        for char in s:
            if char in bracket_map.values():
                # If it's an opening bracket, push to stack
                stack.append(char)
            elif char in bracket_map:
                # If it's a closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
        
        # If stack is empty, all brackets were properly matched
        return len(stack) == 0