#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        sorted_set = set(sorted_nums)
        longest = 0

        for n in nums:
            if (n-1) not in sorted_set:
                length = 0
                while (n+length) in sorted_set:
                    length += 1
                longest = max(length, longest)
        return longest

# Time O(n)
# Memory O(n)

# @lc code=end
