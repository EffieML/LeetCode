#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in t:
            if i in d:
                d[i] -= 1
            else:
                return False
        for i in d:
            if d[i] != 0:
                return False
            else:
                return True

# @lc code=end
