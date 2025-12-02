class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        y_count = Counter()
        for x,y in points:
            y_count[y] += 1

        a_values = []
        for cnt in y_count.values():
            if cnt >= 2:
                a_values.append(cnt * (cnt - 1) // 2 % MOD)

        if len(a_values) < 2:
            return 0

        s = 0
        s2 = 0
        for val in a_values:
            s = (s + val) % MOD
            s2 = (s2 + val * val) % MOD

        result = (s * s - s2) % MOD
        result = result * pow(2, MOD-2, MOD) % MOD

        return result