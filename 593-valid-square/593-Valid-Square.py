from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist_sq(a: List[int], b: List[int]) -> int:
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        pts = [p1, p2, p3, p4]
        dists = sorted(
            dist_sq(pts[i], pts[j])
            for i in range(4)
            for j in range(i + 1, 4)
        )

        return (
            dists[0] > 0
            and dists[0] == dists[1] == dists[2] == dists[3]
            and dists[4] == dists[5]
        )