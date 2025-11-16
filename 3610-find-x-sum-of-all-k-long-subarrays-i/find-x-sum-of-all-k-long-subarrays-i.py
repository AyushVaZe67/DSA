class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n-k+1):
            freq = [0] * 51
            for j in range(i,i+k):
                freq[nums[j]] += 1

            elems = []
            for val in range(1,51):
                if freq[val] > 0:
                    elems.append((freq[val], val))

            elems.sort(key=lambda e: (-e[0], -e[1])) 

            total = 0
            count = min(x ,len(elems))

            for idx in range(count):
                total += elems[idx][0] * elems[idx][1]

            result.append(total)

        return result   
        