from typing import List


# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


def remove_duplicates(nums: List[int]) -> int:
    count = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[count] = nums[i]
            count += 1
    return count


def test_remove_duplicates():
    assert remove_duplicates([1, 1, 2]) == 2
    assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
