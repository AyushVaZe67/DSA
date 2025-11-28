from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        self.components = 0
        
        def dfs(node, parent):
            total = values[node]
            for neighbor in adj[node]:
                if neighbor != parent:
                    total += dfs(neighbor, node)
            if total % k == 0:
                self.components += 1
                return 0
            return total % k
        
        dfs(0, -1)
        return self.components