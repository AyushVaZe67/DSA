from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_seen = {}
        min_distance = float('inf')
        
        for i, num in enumerate(nums):
            # Check if current number is the reverse of any previous number
            # That means: is there a previous number x such that reverse(x) == num?
            # Equivalent to: is there a previous number whose reverse is num?
            # We can store the reverse of each number as we go
            
            # Actually simpler: For each number, we want to know if we've seen a number
            # whose reverse equals the current number
            # So we need to store the reverse of each number we've seen
            
            # But if we store the reverse, then at i=1 with num=21, we check if 21 is in the store
            # At i=0, we stored reverse(120)=21, so yes! distance = 1
            
            # Let's try this:
            pass

# Final working solution:
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_seen = {}
        min_distance = float('inf')
        
        for i, num in enumerate(nums):
            # Check if current number has been seen as the reverse of a previous number
            if num in last_seen:
                distance = i - last_seen[num]
                min_distance = min(min_distance, distance)
            
            # Store the reverse of current number for future checks
            reversed_num = int(str(num)[::-1])
            last_seen[reversed_num] = i
        
        return min_distance if min_distance != float('inf') else -1