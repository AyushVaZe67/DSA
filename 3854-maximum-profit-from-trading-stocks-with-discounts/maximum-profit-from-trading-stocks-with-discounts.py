from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        from collections import defaultdict
        
        children = defaultdict(list)
        for u, v in hierarchy:
            children[u].append(v)
        
        @lru_cache(None)
        def dfs(u, parent_bought):
            cost_u = present[u-1] // 2 if parent_bought else present[u-1]
            profit_u = future[u-1] - cost_u
            
            dp_buy = [-10**9] * (budget + 1)
            dp_not = [-10**9] * (budget + 1)
            dp_not[0] = 0
            
            if cost_u <= budget:
                dp_buy[cost_u] = profit_u
            
            for v in children[u]:
                child_disc = dfs(v, True)
                child_full = dfs(v, False)
                
                new_buy = [-10**9] * (budget + 1)
                new_not = [-10**9] * (budget + 1)
                
                for b1 in range(budget + 1):
                    if dp_buy[b1] > -10**8:
                        for b2 in range(budget - b1 + 1):
                            if child_disc[b2] > -10**8:
                                new_buy[b1 + b2] = max(new_buy[b1 + b2], dp_buy[b1] + child_disc[b2])
                    if dp_not[b1] > -10**8:
                        for b2 in range(budget - b1 + 1):
                            if child_full[b2] > -10**8:
                                new_not[b1 + b2] = max(new_not[b1 + b2], dp_not[b1] + child_full[b2])
                
                dp_buy, dp_not = new_buy, new_not
            
            res = [-10**9] * (budget + 1)
            for b in range(budget + 1):
                res[b] = max(dp_buy[b], dp_not[b])
            return res
        
        dp_root = dfs(1, False)
        return max(dp_root)