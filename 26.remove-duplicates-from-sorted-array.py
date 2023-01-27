#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums), 1):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

# @lc code=end
