#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1,2,3,2,1]
# 1. initialize empty array
# curr_node == head
# curr_node
# space O(n), time O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        curr_node = head
        while curr_node:
            arr.append(curr_node.val)
            next_node = curr_node.next
            curr_node = next_node

        for i in range(len(arr)//2):
            if arr[i] != arr[len(arr)-i-1]:
                return False
        return True


# @lc code=end
