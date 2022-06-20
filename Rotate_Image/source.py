class Solution:
    def rotate(self, matrix: list) -> None:

        """
        Do not return anything, modify matrix in-place instead.
        """

        # Strategy:
        # Since we need to do this in-place, we have to carefully take care of
        # indices. We will perform the following procedure:
        # 1) Save the current pixel value we are working on as temp_current.
        # 2) Find the rotated position where this pixel is going to go.
        # 3) Save that pixel value as temp_new for future use.
        # 4) Replace the pixel value in the rotated position with the current
        # working pixel value: temp_current.
        # 5) Move our current working image position to the rotated position.
        # We do this by updating the current pixel coordinate to the new rotated
        # coordinate. Also update the current pixel value to the original pixel
        # value in the rotated position: temp_new. We do this 4 times in total
        # because these 4 pixels are in a cycle.

        # Notice that we only have to do this for n^2 // 4 times and that we DO NOT
        # want to do these 4-rotations on a pixel that ALREADY HAS BEEN rotated.
        # The pixels that needed to be worked follows this triangular pattern:

        # for 3x3 image:        for 4x4 image:      for 5x5 image:
        # x x .                 x x x .             x x x x .
        # . . .                 . x . .             . x x . .
        # . . .                 . . . .             . . . . .
        #                       . . . .             . . . . .
        #                                           . . . . .

        # for 6x6 image:        for 7x7 image:      for 8x8 image:
        # x x x x x .           x x x x x x .       x x x x x x x .
        # . x x x . .           . x x x x . .       . x x x x x . .
        # . . x . . .           . . x x . . .       . . x x x . . .
        # . . . . . .           . . . . . . .       . . . x . . . .
        # . . . . . .           . . . . . . .       . . . . . . . .
        # . . . . . .           . . . . . . .       . . . . . . . .
        #                       . . . . . . .       . . . . . . . .
        #                                           . . . . . . . .

        # etc, etc.

        # This function takes as input:
        # 1) 2D image coordinate as a list.
        # 2) The center coordinate of the image.
        # 3) Returns the image coordinate rotated 90 degrees clockwise.
        # We do this by translating from image coordinate to cartesian coordinate.
        # Do rotation in cartesian coordinate and translate it back to the image
        # coordinate as a list.
        def get_index_rotated_90_clockwise(coord: list, center_idx):

            # translate to cartesian coordinate where (0,0) is the
            # the center of the image.
            i_translated = coord[0] - center_idx
            j_translated = coord[1] - center_idx

            # Rotate 90 degrees in cartesian coordinate.
            i_rotated = j_translated
            j_rotated = -i_translated

            # Translate back to image coordinate.
            i_new = int(i_rotated + center_idx)
            j_new = int(j_rotated + center_idx)

            return [i_new, j_new]

        # Get the center index of the image. Since we are only dealing with
        # a square image, center index in the x-direction is the same as the
        # center index in the y-direction.
        center_idx = (len(matrix)-1) / 2

        # Initialize the current working image coordinate to [0, 0] and the
        # last working image coordinate to [len(matrix)-1, len(matrix)-1].
        # Notice this is second to the last pixel, not the last corner pixel.
        i = 0
        j = 0
        i_stop = len(matrix) - 1
        j_stop = len(matrix) - 1

        # The 2 nested while loops will go through all the pixels in the image
        # up to the second to the last column and second to the last row.
        while i < i_stop:
            while j < j_stop:

                # 1) Save the current pixel value we are working on as temp_old.
                temp_current = matrix[i][j]

                # For the 4 pixels that are part of the rotation cycle,
                for _ in range(4):

                    # 2) Find the rotated position where the current pixel is going to go.
                    [i_new, j_new] = get_index_rotated_90_clockwise([i, j], center_idx)

                    # 3) Save that pixel value as temp_new for future use.
                    temp_new = matrix[i_new][j_new]

                    # 4) Replace the pixel value in the rotated position with the current
                    # working pixel value: temp_current.
                    matrix[i_new][j_new] = temp_current

                    # 5) Move our current working image position to the rotated position.
                    # We do this by updating the current pixel coordinate to the new rotated
                    # coordinate. Also update the current pixel value to the original pixel
                    # value in the rotated position: temp_new.
                    i = i_new
                    j = j_new
                    temp_current = temp_new

                # The pixels that needed to be worked follows a triangular pattern described
                # above. These indices updates will generate this triangular pattern. Part 1.
                j += 1

            # The pixels that needed to be worked follows a triangular pattern described
            # above. These indices updates will generate this triangular pattern. Part 2.
            i += 1
            j = i
            i_stop -= 1
            j_stop -= 1

        return None


m = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]

Solution().rotate(m)
print(m)
