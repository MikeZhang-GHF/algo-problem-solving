from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    #  divide
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    # conquer
    i, j, cur = 0, 0, 0
    n, m = len(left), len(right)
    while True:
        if i == n:
            nums[cur:] = right[j:]
            break
        if j == m:
            nums[cur:] = left[i:]
            break
        if left[i] <= right[j]:
            nums[cur] = left[i]
            cur, i = cur + 1, i + 1
        else:
            nums[cur] = right[j]
            cur, j = cur + 1, j + 1
    return nums


a = [3, 5, 2, 1, 4]
print(merge_sort(a))
