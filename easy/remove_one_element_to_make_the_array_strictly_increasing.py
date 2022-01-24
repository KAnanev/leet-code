# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/submissions/

from typing import List


def can_be_increasing(nums: List[int]) -> bool:
    prev, seen = 0, False
    for i, item in enumerate(nums):
        if prev < item:
            prev = item
        else:
            if seen:
                return False
            seen = True
            if i == 1 or nums[i - 2] < item:
                prev = item
    return True
