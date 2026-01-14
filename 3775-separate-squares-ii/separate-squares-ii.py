from typing import List
from bisect import bisect_right

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        # Each square creates two Y-events:
        # enter at y, exit at y + side, carrying its x-interval
        class Event:
            def __init__(self, y, type_, x, side):
                self.y = y
                self.type = type_   # +1 = enter, -1 = exit
                self.x = x
                self.side = side

        # Segment tree over compressed x-intervals
        # Maintains UNION length of active x-intervals
        class SegmentTree:
            def __init__(self, xs):
                self.xs = xs
                self.n = len(xs) - 1
                self.coverCount = [0] * (4 * self.n)
                self.coveredLen = [0.0] * (4 * self.n)

            # Update coverage on [ql, qr) with +1 (add) or -1 (remove)
            def update(self, node, left, right, ql, qr, delta):
                if qr <= left or right <= ql:
                    return

                if ql <= left and right <= qr:
                    self.coverCount[node] += delta
                else:
                    mid = (left + right) // 2
                    self.update(node * 2, left, mid, ql, qr, delta)
                    self.update(node * 2 + 1, mid, right, ql, qr, delta)

                if self.coverCount[node] > 0:
                    self.coveredLen[node] = self.xs[right] - self.xs[left]
                elif left + 1 == right:
                    self.coveredLen[node] = 0.0
                else:
                    self.coveredLen[node] = (
                        self.coveredLen[node * 2] +
                        self.coveredLen[node * 2 + 1]
                    )

        # ---- Build events and collect x-coordinates ----
        events = []
        xSet = set()

        for x, y, side in squares:
            events.append(Event(y, 1, x, side))          # enter
            events.append(Event(y + side, -1, x, side))  # exit
            xSet.add(x)
            xSet.add(x + side)

        # ---- Coordinate compression on x ----
        xs = sorted(xSet)
        xIndex = {xs[i]: i for i in range(len(xs))}

        # sort events by y
        events.sort(key=lambda e: e.y)

        # ---- First sweep: compute total union area ----
        st = SegmentTree(xs)
        totalArea = 0.0
        prevY = events[0].y

        for e in events:
            currY = e.y
            totalArea += st.coveredLen[1] * (currY - prevY)

            st.update(
                1, 0, st.n,
                xIndex[e.x],
                xIndex[e.x + e.side],
                e.type
            )
            prevY = currY

        half = totalArea / 2.0

        # ---- Second sweep: find smallest y where area reaches half ----
        st = SegmentTree(xs)
        areaSoFar = 0.0
        prevY = events[0].y

        for e in events:
            currY = e.y
            width = st.coveredLen[1]
            dy = currY - prevY

            if areaSoFar + width * dy >= half:
                return prevY + (half - areaSoFar) / width

            areaSoFar += width * dy

            st.update(
                1, 0, st.n,
                xIndex[e.x],
                xIndex[e.x + e.side],
                e.type
            )
            prevY = currY

        return prevY
