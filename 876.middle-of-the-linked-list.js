/*
 * @lc app=leetcode id=876 lang=javascript
 *
 * [876] Middle of the Linked List
 */

// @lc code=start
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

// mid is always about half of total length, move end by 2 to find the end node, meanwhile move mid by 1;
var middleNode = function (head) {
    let mid = head;
    let end = head;

    while (end !== null && end.next !== null) {
        mid = mid.next;
        end = end.next.next;
    }

    return mid;
};

// time complexity O(n) -> O(n/1)
// space complexity O(1)
// @lc code=end
