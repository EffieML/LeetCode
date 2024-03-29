#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    # def alphaNum(self, c):
    #     return (ord('A') <= ord(c) <= ord('Z') or
    #             ord('a') <= ord(c) <= ord('z') or
    #             ord('0') <= ord(c) <= ord('9'))

    # def isPalindrome(self, s: str) -> bool:
    #     l, r = 0, len(s)-1
    #     while l < r:
    #         while l < r and not self.alphaNum(s[l]):
    #             l += 1
    #         while r > l and not self.alphaNum(s[r]):
    #             r -= 1
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l, r = l + 1, r - 1
    #     return True
    # time O(n), memory O(1)

    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


# @lc code=end
