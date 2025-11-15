import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros_pos = [i for i, ch in enumerate(s) if ch == '0']
        m = len(zeros_pos)
        ans = 0

        # z = 0 case: all-ones substrings
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                L = j - i
                ans += L * (L + 1) // 2
                i = j
            else:
                i += 1

        if m == 0:
            return ans  # all substrings already counted

        z_max = int(math.isqrt(n))  # max zeros to consider (z^2 <= n)
        z_max = min(z_max, m)

        for z in range(1, z_max + 1):
            # slide window over zeros_pos: windows of size z
            for start in range(0, m - z + 1):
                left_zero_idx = start
                right_zero_idx = start + z - 1
                posL = zeros_pos[left_zero_idx]
                posR = zeros_pos[right_zero_idx]

                prev_zero_pos = zeros_pos[left_zero_idx - 1] if left_zero_idx > 0 else -1
                next_zero_pos = zeros_pos[right_zero_idx + 1] if right_zero_idx + 1 < m else n

                left_ones = posL - prev_zero_pos - 1
                right_ones = next_zero_pos - posR - 1

                base_len = posR - posL + 1
                base_ones = base_len - z

                req = z * z - base_ones  # need l + r >= req
                if req <= 0:
                    # all extension choices valid
                    ans += (left_ones + 1) * (right_ones + 1)
                    continue

                L = left_ones
                R = right_ones
                total_pairs = (L + 1) * (R + 1)
                if req > L + R:
                    # cannot satisfy
                    continue

                # Count number of pairs with l + r <= T  where T = req - 1 (these are invalid)
                T = req - 1
                # If T >= L+R then all are invalid (but we handled req > L+R above)
                # Compute invalid in O(1)
                a = max(0, T - R)       # l starts from 0 to a-1 => r limited by R, contributes (R+1) each
                b = min(L, T)           # last l to consider in second sum
                if a > b:
                    # all l in [0..b] fall in first form? actually if a > b then no second part
                    invalid = (b + 1) * (R + 1)  # since a>b, effectively all considered l are in first part
                else:
                    # first part: l=0..a-1 => each contributes (R+1)
                    first = a * (R + 1)
                    # second part: l=a..b => each contributes (T - l + 1)
                    cnt = b - a + 1
                    # sum_{l=a}^{b} (T+1) - sum_{l=a}^{b} l
                    second = cnt * (T + 1) - (a + b) * cnt // 2
                    invalid = first + second

                valid = total_pairs - invalid
                ans += valid

        return ans
