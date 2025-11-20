class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1], -x[0]))
        result = 0
        largest = [-1,-1]

        for start, end in intervals:
            if start > largest[1]:
                result += 2
                largest = [end -1, end]
            elif start > largest[0]:
                result += 1
                largest = [largest[1], end]

        return result
        