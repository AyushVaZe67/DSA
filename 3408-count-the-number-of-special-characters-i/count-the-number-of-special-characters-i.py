class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase_set = set()
        uppercase_set = set()
        
        # Track all lowercase and uppercase letters present
        for char in word:
            if char.islower():
                lowercase_set.add(char)
            else:
                uppercase_set.add(char.lower())  # Store uppercase as lowercase for comparison
        
        # Count letters that appear in both sets
        count = 0
        for char in lowercase_set:
            if char in uppercase_set:
                count += 1
        
        return count