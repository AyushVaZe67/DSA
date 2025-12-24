class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)

        curr = 0
        for i,c in enumerate(capacity):
            curr += c
            if curr >= total:
                return i + 1

        return len(capacity)