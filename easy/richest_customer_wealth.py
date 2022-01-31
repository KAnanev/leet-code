# https://leetcode.com/problems/richest-customer-wealth/

from typing import List


def maximum_wealth(accounts: List[List[int]]) -> int:
    return max(map(sum, accounts))
