from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Transform array: +1 for target, -1 otherwise
        arr = [1 if num == target else -1 for num in nums]
        
        # Prefix sums, starting with 0
        prefix = [0]
        for val in arr:
            prefix.append(prefix[-1] + val)
        
        # Count pairs (i, j) with i < j and prefix[i] < prefix[j]
        # We'll use a Fenwick tree to count how many previous prefix sums
        # are less than current prefix sum
        
        # Coordinate compression for prefix sums
        sorted_prefix = sorted(prefix)
        rank = {val: idx + 1 for idx, val in enumerate(sorted_prefix)}  # 1-indexed for BIT
        
        bit = [0] * (len(prefix) + 2)
        
        def update(idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & -idx
        
        def query(idx):
            sum_val = 0
            while idx > 0:
                sum_val += bit[idx]
                idx -= idx & -idx
            return sum_val
        
        count = 0
        for p in prefix:
            # Count how many previous prefix sums are < p
            # We need to query for rank(p) - 1
            idx = rank[p] - 1
            count += query(idx)
            # Insert current prefix sum
            update(rank[p], 1)
        
        return count