from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        total_decrements = sum(nums)

        if total_decrements == 0:
            # each zero index contributes 2 choices (left/right)
            return nums.count(0) * 2

        def simulate(start: int, direction: int) -> bool:
            # quick local alias
            arr = nums
            changed = []  # list of (idx, times_decremented)
            curr = start
            steps = 0
            # We will allow at most total_decrements * (n + 2) steps as a safe cap.
            # Real necessary steps are bounded by something like total_decrements * n,
            # but this cap prevents runaway loops on pathological inputs.
            step_cap = (total_decrements + 1) * (n + 2)

            while 0 <= curr < n:
                if steps > step_cap:
                    # too many steps -> abort (treat as failure)
                    break
                if arr[curr] == 0:
                    curr += direction
                else:
                    # decrement and record
                    arr[curr] -= 1
                    if not changed or changed[-1][0] != curr:
                        changed.append([curr, 1])
                    else:
                        # increment the count for the same index
                        changed[-1][1] += 1
                    # reverse direction and step
                    direction = -direction
                    curr += direction
                steps += 1

            # finished: check all zeros
            ok = all(x == 0 for x in arr)

            # revert changes
            for idx, cnt in changed:
                arr[idx] += cnt

            return ok

        ans = 0
        for i in range(n):
            if nums[i] == 0:
                if simulate(i, 1):
                    ans += 1
                if simulate(i, -1):
                    ans += 1

        return ans
