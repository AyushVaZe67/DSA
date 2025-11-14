class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # diff matrix must be (n+1) x (n+1)
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Prefix row-wise
        for r in range(n):
            curr = 0
            for c in range(n):
                curr += diff[r][c]
                diff[r][c] = curr     # fixed: = not ==

        # Prefix column-wise
        for c in range(n):
            curr = 0
            for r in range(n):
                curr += diff[r][c]
                diff[r][c] = curr

        # return n x n matrix
        return [row[:n] for row in diff[:n]]
