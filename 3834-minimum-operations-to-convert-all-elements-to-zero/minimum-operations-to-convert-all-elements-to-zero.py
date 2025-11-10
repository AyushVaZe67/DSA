class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        operations = 0
        
        for num in nums:
            # Pop from stack while top is >= current number
            while stack and stack[-1] >= num:
                if stack[-1] > num:
                    operations += 1
                stack.pop()
            
            if num > 0:
                stack.append(num)
        
        # Add operations for remaining elements in stack
        operations += len(stack)
        
        return operations