#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (39.05%)
# Likes:    14620
# Dislikes: 606
# Total Accepted:    1.9M
# Total Submissions: 4.6M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
#
# Example 2:
#
#
# Input: head = [1], n = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
#
# Follow up: Could you do this in one pass?
#
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use 2 pointers, L at dummy, R at dummy + n+1 node, move both
        # T = O(n), M = O(1)
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        # delete the nth node
        left.next = left.next.next
        return dummy.next

# @lc code=end
