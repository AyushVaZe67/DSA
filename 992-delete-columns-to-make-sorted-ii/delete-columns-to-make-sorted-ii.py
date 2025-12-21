class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        sorted_pairs = [False] * (n-1)
        d = 0

        for col in range(m):
            delete = False
            for i in range(n-1):
                if not sorted_pairs[i] and strs[i][col] > strs[i+1][col]:
                    delete = True
                    break

            if delete:
                d += 1
            else:
                for i in range(n-1):
                    if strs[i][col] < strs[i+1][col]:
                        sorted_pairs[i] = True

        return d