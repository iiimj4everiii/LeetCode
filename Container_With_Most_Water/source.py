class Solution:
    def maxArea(self, height) -> int:

        # Initialize i, j and max_area
        i = 0
        j = len(height)-1
        max_area = 0

        # Start from the edges, find the area.
        # The area equals to the min(left_height, right_height) * (right_idx - left_idx).
        # Update the max_area of the current area is greater.
        # Then scans the heights inwards, skipping those that are shorter than min(left_height, right_height).
        # This is because the areas using those heights will always be less than min(left_height, right_height)
        # on the outer layers. If an inner height is taller, check to see if the area created is greater than
        # our max_area so far. Update max_area if the new area is greater.
        while i < j:
            h = min(height[i], height[j])
            area = h * (j-i)
            max_area = max(max_area, area)

            # Skip subsequent heights that are lower than or equals to h
            while h >= height[i] and i < j:
                i += 1

            # Skip subsequent heights that are lower than or equals to h
            while h >= height[j] and i < j:
                j -= 1

        return max_area


h = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(h))
