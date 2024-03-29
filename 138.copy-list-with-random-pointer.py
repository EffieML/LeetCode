#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (49.67%)
# Likes:    10636
# Dislikes: 1129
# Total Accepted:    917.9K
# Total Submissions: 1.8M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# A linked list of length n is given such that each node contains an additional
# random pointer, which could point to any node in the list, or null.
#
# Construct a deep copy of the list. The deep copy should consist of exactly n
# brand new nodes, where each new node has its value set to the value of its
# corresponding original node. Both the next and random pointer of the new
# nodes should point to new nodes in the copied list such that the pointers in
# the original list and copied list represent the same list state. None of the
# pointers in the new list should point to nodes in the original list.
#
# For example, if there are two nodes X and Y in the original list, where
# X.random --> Y, then for the corresponding two nodes x and y in the copied
# list, x.random --> y.
#
# Return the head of the copied linked list.
#
# The linked list is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
#
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random
# pointer points to, or null if it does not point to any node.
#
#
# Your code will only be given the head of the original linked list.
#
#
# Example 1:
#
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
# Example 2:
#
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
#
# Example 3:
#
#
#
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
#
#
# Constraints:
#
#
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random is null or is pointing to some node in the linked list.
#
#
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# iterate through the linked list twice
# first time store the linked list Value
# 2nd time store the pointers
# used hash map to easy get the value info
# T = O(n) 2 iterations; M=O(n) hash map extra space


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldCopy[cur]
            copy.next = oldCopy[cur.next]
            copy.random = oldCopy[cur.random]
            cur = cur.next
        # print("hash map: ", oldCopy)
        # print("linked list copy: ", oldCopy[head].val)
        return oldCopy[head]


# @lc code=end

# # Test
# # head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
# head = Node(7)
# head.next = Node(13)
# head.next.next = Node(11)
# head.next.next.next = Node(10)
# head.next.next.next.next = Node(1)
# head.next.random = head
# head.next.next.next.random = head.next.next
# head.next.next.random = head.next.next.next.next
# test = Solution()
# test.copyRandomList(head)
