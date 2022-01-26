# https://leetcode.com/problems/koko-eating-bananas/submissions/
import math
from typing import List


def min_eating_speed(piles: List[int], h: int) -> int:
    count_bananas = 1
    max_bananas_in_hours = max(piles)

    while count_bananas < max_bananas_in_hours:
        middle = (count_bananas + max_bananas_in_hours) // 2

        if sum(math.ceil(pile / middle) for pile in piles) <= h:
            max_bananas_in_hours = middle
        else:
            count_bananas = middle + 1

    return max_bananas_in_hours
