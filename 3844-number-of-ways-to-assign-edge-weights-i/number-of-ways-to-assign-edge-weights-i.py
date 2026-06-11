from typing import List
from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        if not edges:
            return 0
            
        # Build graph
        graph = defaultdict(list)
        n = len(edges) + 1
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS to find max depth and path to that node
        parent = {1: None}
        depth = {1: 0}
        
        queue = deque([1])
        max_depth = 0
        max_depth_nodes = []
        
        while queue:
            node = queue.popleft()
            
            if depth[node] > max_depth:
                max_depth = depth[node]
                max_depth_nodes = [node]
            elif depth[node] == max_depth:
                max_depth_nodes.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in parent:
                    parent[neighbor] = node
                    depth[neighbor] = depth[node] + 1
                    queue.append(neighbor)
        
        # Get path from root to first max depth node
        target = max_depth_nodes[0]
        path_length = 0
        node = target
        
        while node != 1:
            path_length += 1
            node = parent[node]
        
        # Number of ways = 2^(path_length-1)
        # Need modular exponentiation
        result = pow(2, path_length - 1, MOD)
        
        return result