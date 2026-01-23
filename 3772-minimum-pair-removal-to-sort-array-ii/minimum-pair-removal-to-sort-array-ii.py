from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Doubly linked list simulation
        prev = list(range(-1, n - 1))
        next = list(range(1, n + 1))
        next[n - 1] = -1

        alive = [True] * n

        # Count decreasing violations
        violations = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                violations += 1

        # Min-heap of (sum, index)
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        ops = 0

        while violations > 0:
            pair_sum, i = heapq.heappop(heap)

            # Skip invalid pairs
            if not alive[i]:
                continue
            j = next[i]
            if j == -1 or not alive[j]:
                continue
            if nums[i] + nums[j] != pair_sum:
                continue

            # Remove old violations
            pi = prev[i]
            nj = next[j]

            if pi != -1 and nums[pi] > nums[i]:
                violations -= 1
            if nums[i] > nums[j]:
                violations -= 1
            if nj != -1 and nums[j] > nums[nj]:
                violations -= 1

            # Merge
            nums[i] += nums[j]
            alive[j] = False
            next[i] = nj
            if nj != -1:
                prev[nj] = i

            # Add new violations
            if pi != -1 and nums[pi] > nums[i]:
                violations += 1
            if nj != -1 and nums[i] > nums[nj]:
                violations += 1

            # Push new adjacent sums
            if pi != -1:
                heapq.heappush(heap, (nums[pi] + nums[i], pi))
            if nj != -1:
                heapq.heappush(heap, (nums[i] + nums[nj], i))

            ops += 1

        return ops
