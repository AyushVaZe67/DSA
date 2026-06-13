from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:
            # Calculate weight of the word
            weight_sum = 0
            for char in word:
                # Get index of character (0 for 'a', 1 for 'b', etc.)
                idx = ord(char) - ord('a')
                weight_sum += weights[idx]
            
            # Take modulo 26
            mod_result = weight_sum % 26
            
            # Map to letter using reverse alphabetical order
            # 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            mapped_char = chr(ord('z') - mod_result)
            result.append(mapped_char)
        
        return ''.join(result)