# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ...,
# (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

# Input: nums = [1,4,3,2]
# Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.

# Solution 1
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if (len(pair) == 2):
                print(min(pair))
                sum += min(pair)
                pair = []

        return sum

# Solution 2
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n

        return sum
# Solution 3
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])