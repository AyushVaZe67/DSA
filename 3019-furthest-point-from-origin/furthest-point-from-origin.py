class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left_count = moves.count('L')
        right_count = moves.count('R')
        wild_count = moves.count('_')
        
        # Maximum position when going right
        max_right = right_count + wild_count - left_count
        
        # Maximum position when going left (negative)
        max_left = right_count - (left_count + wild_count)
        
        # Return the maximum absolute distance
        return max(abs(max_right), abs(max_left))