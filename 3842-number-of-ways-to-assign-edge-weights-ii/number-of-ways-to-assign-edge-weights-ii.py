from typing import List
from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1  # Number of nodes
        
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Prepare for binary lifting LCA
        LOG = (n).bit_length()
        parent = [[-1] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        
        # BFS to compute parent[0] and depth
        queue = deque([1])
        depth[1] = 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor != parent[0][node] and neighbor != 1:
                    parent[0][neighbor] = node
                    depth[neighbor] = depth[node] + 1
                    queue.append(neighbor)
        
        # Build binary lifting table
        for k in range(1, LOG):
            for i in range(1, n + 1):
                if parent[k-1][i] != -1:
                    parent[k][i] = parent[k-1][parent[k-1][i]]
        
        # Precompute powers of 2 modulo MOD
        pow2 = [1] * (n + 2)
        for i in range(1, n + 2):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            # Lift u to same depth as v
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]
            
            if u == v:
                return u
            
            # Lift both u and v
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v] and parent[k][u] != -1 and parent[k][v] != -1:
                    u = parent[k][u]
                    v = parent[k][v]
            
            return parent[0][u]
        
        # Process queries
        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
            else:
                ancestor = lca(u, v)
                path_length = depth[u] + depth[v] - 2 * depth[ancestor]
                answer.append(pow2[path_length - 1])
        
        return answer