class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        if n == 1:
            return m % MOD
        
        if n == 2:
            # All pairs with different values
            return (m * (m - 1)) % MOD
        
        # For length >= 3, we can use the fact that the transition is linear
        # We'll use matrix exponentiation with size 2*m
        
        # However, we can do even better: reduce to 2x2 block matrix
        # Let's use the fact that transitions are:
        # new_inc[x] = prefix_sum_dec[x-1]
        # new_dec[x] = suffix_sum_inc[x+1]
        
        # Instead of tracking each value, track prefix sums
        # Let P_inc[i] = sum_{x=0}^{i} inc[x]
        # Let P_dec[i] = sum_{x=0}^{i} dec[x]
        # Then:
        # new_inc[x] = P_dec[x-1]
        # new_dec[x] = total_inc - P_inc[x]
        
        # We can track P_inc and P_dec arrays
        # But we still need per-value for next step's prefix sums
        
        # Actually, let's just use matrix exponentiation with size m
        # since inc and dec are symmetric
        
        # Even better: recognize that inc[x] and dec[m-1-x] are related
        # For length 2: inc[x] = dec[m-1-x] = x
        # This symmetry holds throughout
        
        # So we only need to track one array: inc[x]
        # dec[x] = inc[m-1-x]
        # Let's verify: new_inc[x] = sum_{v<x} dec[v] = sum_{v<x} inc[m-1-v]
        # new_dec[x] = sum_{v>x} inc[v]
        # And new_dec[x] should equal new_inc[m-1-x]
        # new_inc[m-1-x] = sum_{v < m-1-x} dec[v] = sum_{v < m-1-x} inc[m-1-v]
        # Let u = m-1-v, then v = m-1-u, and v < m-1-x => m-1-u < m-1-x => u > x
        # So new_inc[m-1-x] = sum_{u > x} inc[u] = new_dec[x] ✓
        
        # So symmetry holds, we only track inc of size m
        # Transition: new_inc[x] = sum_{v=0}^{x-1} inc[m-1-v]
        # = sum_{u=m-x}^{m-1} inc[u] (where u = m-1-v)
        # = suffix_sum_inc[m-x]
        
        # So new_inc[x] = suffix_sum_inc[m-x]
        # Which is a linear transformation on inc
        
        size = m
        trans = [[0] * size for _ in range(size)]
        
        for x in range(m):
            # new_inc[x] = sum_{u=m-x}^{m-1} inc[u]
            for u in range(m - x, m):
                trans[x][u] = 1
        
        # Initial state for length 2: inc[x] = x
        init = [i % MOD for i in range(m)]
        
        if n == 2:
            return (2 * sum(init)) % MOD
        
        # Matrix exponentiation
        def mat_mul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                for k in range(n):
                    if A[i][k]:
                        aik = A[i][k]
                        Bk = B[k]
                        for j in range(n):
                            C[i][j] = (C[i][j] + aik * Bk[j]) % MOD
            return C
        
        def mat_pow(mat, exp):
            n = len(mat)
            res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            while exp:
                if exp & 1:
                    res = mat_mul(res, mat)
                mat = mat_mul(mat, mat)
                exp >>= 1
            return res
        
        # Apply transition (n-2) times
        trans_pow = mat_pow(trans, n - 2)
        
        # Compute final inc
        final_inc = [0] * size
        for i in range(size):
            total = 0
            for j in range(size):
                total = (total + trans_pow[i][j] * init[j]) % MOD
            final_inc[i] = total
        
        # Total = sum(inc) + sum(dec) = 2 * sum(inc)
        return (2 * sum(final_inc)) % MOD