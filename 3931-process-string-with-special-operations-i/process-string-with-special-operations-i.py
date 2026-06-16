class Solution:
    def processStr(self, s: str) -> str:
        result = []
        
        for char in s:
            if char.islower():  # lowercase English letter
                result.append(char)
            elif char == '*':
                if result:  # only remove if result is not empty
                    result.pop()
            elif char == '#':
                # Duplicate: result = result + result
                result = result + result[:]  # create a copy of the current list
            elif char == '%':
                # Reverse the result
                result = result[::-1]
        
        return ''.join(result)