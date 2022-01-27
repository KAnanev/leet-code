# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

def find_maximum_xor(nums):
    m, mask = 0, 0

    for i in range(32)[::-1]:
        mask |= 1 << i
        prefixes = {n & mask for n in nums}

        tmp = m | (1 << i)

        if any(prefix ^ tmp in prefixes for prefix in prefixes):
            m = tmp

    return m
