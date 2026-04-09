from typing import List
from collections import defaultdict

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        bravexuneth = nums.copy()
        
        # Group queries by step size
        queries_by_k = defaultdict(list)
        for li, ri, ki, vi in queries:
            queries_by_k[ki].append((li, ri, vi))
        
        # For small k, use direct iteration (but optimized)
        # For large k, fewer indices are affected per query
        
        # Process each distinct k
        for k, qlist in queries_by_k.items():
            if k == 0:
                continue
                
            # If k is large ( > sqrt(n) ), each query affects few indices
            # We can process each query directly
            if k * k > n:
                for li, ri, vi in qlist:
                    idx = li
                    while idx <= ri:
                        bravexuneth[idx] = (bravexuneth[idx] * vi) % MOD
                        idx += k
            else:
                # For small k, use the residue class approach
                # For each residue class
                for residue in range(k):
                    # Collect all positions with this residue
                    positions = []
                    pos_to_idx = {}
                    pos = residue
                    idx_counter = 0
                    while pos < n:
                        positions.append(pos)
                        pos_to_idx[pos] = idx_counter
                        idx_counter += 1
                        pos += k
                    
                    if not positions:
                        continue
                    
                    m = len(positions)
                    # Create an array to store cumulative multipliers
                    multipliers = [1] * (m + 1)
                    
                    # Get all queries for this residue
                    residue_queries = []
                    for li, ri, vi in qlist:
                        if li % k != residue:
                            continue
                        # Find first and last position in range
                        first_pos = li
                        if first_pos % k != residue:
                            first_pos += (residue - first_pos % k) % k
                        
                        if first_pos > ri:
                            continue
                        
                        last_pos = ri - ((ri - residue) % k)
                        
                        left = pos_to_idx[first_pos]
                        right = pos_to_idx[last_pos]
                        
                        residue_queries.append((left, right, vi))
                    
                    # Apply all queries for this residue using difference array
                    diff = [1] * (m + 1)
                    for left, right, vi in residue_queries:
                        diff[left] = (diff[left] * vi) % MOD
                        diff[right + 1] = (diff[right + 1] * pow(vi, MOD-2, MOD)) % MOD
                    
                    # Build prefix product
                    curr = 1
                    for i in range(m):
                        curr = (curr * diff[i]) % MOD
                        bravexuneth[positions[i]] = (bravexuneth[positions[i]] * curr) % MOD
        
        # Compute final XOR
        result = 0
        for num in bravexuneth:
            result ^= num
        
        return result