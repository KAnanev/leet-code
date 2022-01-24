# https://leetcode.com/problems/can-place-flowers/
from typing import List


def can_place_flowers(flowerbed: List[int], n: int) -> bool:

    tmp = [0] + flowerbed + [0]

    for i in range(1, len(tmp) - 1):
        if not tmp[i - 1] and not tmp[i] and not tmp[i + 1]:
            tmp[i] = 1
            n -= 1
    return n <= 0


def test_can_place_flowers():
    assert can_place_flowers([1, 0, 0, 0, 1], 1)
    assert not can_place_flowers([1, 0, 0, 0, 1], 2)
    assert can_place_flowers([1, 0, 0, 0, 1, 0, 0], 2)
    assert can_place_flowers([1, 0, 0, 0, 0, 0, 1], 2)


