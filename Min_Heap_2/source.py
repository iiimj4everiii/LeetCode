def get_left_child_index(current_index) -> int:
    return 2 * current_index + 1


def heapify(nums, index) -> list:

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
        (smaller_child, smaller_child_index) = min((left_child, left_child_index),(right_child, right_child_index))
        if smaller_child < nums[index]:
            nums[index], nums[smaller_child_index] = nums[smaller_child_index], nums[index]
            nums = heapify(nums, smaller_child_index)

    return nums


def build_heap_bottom_up(nums) -> list:

    last_non_leaf_node_index = len(nums) // 2 - 1
    for idx in range(last_non_leaf_node_index, -1, -1):
        nums = heapify(nums, idx)

    return nums


num = [5, 8, 1, 3, 7, 0, 2, 9, 6]
num = build_heap_bottom_up(num)
print(num)
