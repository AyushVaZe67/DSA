class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        minStart = [0] * (n + 1)
        max_q = deque()
        min_q = deque()

        L = 0
        for R in range(n):
            while max_q and nums[max_q[-1]] <= nums[R]:
                max_q.pop()
            max_q.append(R)

            while min_q and nums[min_q[-1]] >= nums[R]:
                min_q.pop()
            min_q.append(R)

            while nums[max_q[0]] - nums[min_q[0]] > k:
                if max_q[0] == L:
                    max_q.popleft()
                if min_q[0] == L:
                    min_q.popleft()
                L += 1
            
            minStart[R+1] = L

        dp = [0] * (n+1)
        prefix = [0] * (n+1)
        dp[0] = 1
        prefix[0] = 1

        for i in range(1, n+1):
            if minStart[i] > 0:
                dp[i] = (prefix[i-1] - prefix[minStart[i]-1]) % MOD
            else:
                dp[i] = prefix[i-1] % MOD
            prefix[i] = (prefix[i-1] + dp[i]) % MOD

        return dp[n] % MOD
        