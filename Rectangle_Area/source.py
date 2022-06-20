class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        # Strategy:
        # Total area covered by the two rectangles is equal to:
        # area1 + area2 - intersect(area1, area2)
        # area1 = (ax2 - ax1) * (ay2 - ay1)
        # area2 = (bx2 - bx1) * (by2 - by1)

        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        total_area = area1 + area2

        # If these two rectangles intersect in the x-axis and in
        # the y-axis, then there is an intersection area. We will
        # calculate the intersection area and remove it from the
        # sum of area at the end. In order to see if there is an
        # intersection in the x-axis, W.L.O.G. we check if the left
        # side of 1 rectangle is sandwiched between the left side
        # and the right side of the second rectangle. The same
        # principle applies to the y-axis.
        intersection = 0
        if (ax1 <= bx1 <= ax2 or bx1 <= ax1 <= bx2) and\
           (ay1 <= by1 <= ay2 or by1 <= ay1 <= by2):

            # No matter how they overlap, the left side of the the over-
            # lapping area is the MAX(ax1, bx1) and the right side of
            # the overlapping area is MIN(ax2, bx2). Likewise, the bottom
            # of the overlapping area is the MAX(ay1, by1) and the top of
            # the overlapping area is the MIN(ay2, by2). Therefore, the
            # overlapping/intersection area is equal to:
            # intersection = (right - left) * (top - bottom).

            left = max(ax1, bx1)
            right = min(ax2, bx2)

            bottom = max(ay1, by1)
            top = min(ay2, by2)

            intersection = (right - left) * (top - bottom)

        return total_area - intersection


sol = Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
# sol = Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2)
print(sol)
