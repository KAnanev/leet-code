# https://leetcode.com/problems/valid-mountain-array/solution/
from typing import List


def valid_mountain_array(arr: List[int]) -> bool:
    result = True

    if len(arr) < 3 or arr[0] >= arr[1]:
        return False

    for i in range(1, len(arr)):

        if result:
            if arr[i - 1] >= arr[i]:
                result = False

        if not result:
            if arr[i - 1] <= arr[i]:
                return result

    return not result
