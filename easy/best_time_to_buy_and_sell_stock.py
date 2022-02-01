# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

from typing import List


def max_profit(prices: List[int]) -> int:
    left, right = 0, 1
    profit = 0

    while right < len(prices):
        if prices[right] > prices[left]:
            current_profit = prices[right] - prices[left]
            profit = max(current_profit, profit)
        else:
            left = right
        right += 1
    return profit
