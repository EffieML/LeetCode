#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # d = {}
        # for i in range(len(nums)):
        #     if target - nums[i] in d:
        #         return [i, d[target-nums[i]]]
        #     else:
        #         d[nums[i]] = i

        d = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in d:
                return [d[diff], i]
            d[n] = i
# time O(n) worst time O(n^2), space O(n)
# @lc code=end
