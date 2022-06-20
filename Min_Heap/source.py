# Given a list representing a "complete" binary tree, the index of the left child is located at
# index = 2 * current_index + 1.
def get_left_child_index(current_index):
    return 2 * current_index + 1


def heapify(nums, index):

    left_child_index = get_left_child_index(index)
    left_child = None
    if left_child_index < len(nums):
        left_child = nums[left_child_index]

    if left_child is None:
        return nums

    right_child_index = left_child_index + 1
    right_child = None
    if right_child_index < len(nums):
        right_child = nums[right_child_index]

    if right_child is None:
        if left_child < nums[index]:
            nums[index], nums[left_child_index] = nums[left_child_index], nums[index]
            nums = heapify(nums, left_child_index)
    
    else:
        (_, smaller_child_index) = min((left_child, left_child_index), (right_child, right_child_index))
        if nums[smaller_child_index] < nums[index]:
            nums[index], nums[smaller_child_index] = nums[smaller_child_index], nums[index]
            nums = heapify(nums, smaller_child_index)

    return nums


# This is the most efficient way to build a heap (from bottom up).
# We treat nums:list as a complete binary whose nodes are randomly
# distributed among themselves in the tree. Then we heapify all the
# nodes on the tree starting from the last non-leaf node.
def build_heap_bottom_up(nums):

    # We can skip all the leaf nodes on this tree since they are
    # already in the correct heap configuration. Starting_index is
    # the last non-leaf node.
    starting_index = len(nums) // 2 - 1
    for i in range(starting_index, -1, -1):
        nums = heapify(nums, i)

    return nums


num = [5, 8, 1, 3, 7, 0, 2]
#           5
#       8       1
#     3   7   0   2

num = build_heap_bottom_up(num)
print(num)
