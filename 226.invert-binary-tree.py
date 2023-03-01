#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (74.50%)
# Likes:    11762
# Dislikes: 166
# Total Accepted:    1.5M
# Total Submissions: 2M
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Given the root of a binary tree, invert the tree, and return its root.
#
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
#
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
# The time complexity is O(n), where n is the number of nodes in the tree. This is because each node in the tree is visited exactly once, and the time complexity of swapping the children is constant time.
# The space complexity of the method is O(h), where h is the height of the tree. This is because the method uses a recursive approach to traverse the tree, and the maximum number of function calls on the call stack is equal to the height of the tree. In the worst case, when the tree is skewed and has a height of n, the space complexity would be O(n). However, in a balanced tree, the space complexity would be O(log n).

# @lc code=end
