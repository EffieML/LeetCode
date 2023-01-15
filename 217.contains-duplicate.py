#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
       # nums_set = set()
       # for num in nums:
       #     if num in nums_set:
       #         return True
       #     nums_set.add(num)
       # return False


# @lc code=end
