class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)

        left = 0
        while left < n and directions[left] == 'L':
            left += 1

        right = n
        while right > 0 and directions[right - 1] == 'R':
            right -= 1

        count = 0
        for i in range(left, right):
            if directions[i] != 'S':
                count += 1
            
        if count > 0:
            return count
        else:
            return 0


        