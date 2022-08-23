/*
 * @lc app=leetcode id=148 lang=javascript
 *
 * [148] Sort List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */


var sortList = function (head) {
    if (head === null || head.next === null) return head;

    let mid = getMid(head);
    let leftsort = sortList(head);
    let rightsort = sortList(mid);
    return merge(leftsort, rightsort);
};

function merge(list1, list2) {
    let newHead = new ListNode();
    let tail = new ListNode();
    tail = newHead;

    // iterate through listA and listB, add the smaller one to the new list
    while (list1 !== null && list2 !== null) {
        if (list1.val < list2.val) {
            tail.next = list1;
            list1 = list1.next;
            tail = tail.next;
        } else {
            tail.next = list2;
            list2 = list2.next;
            tail = tail.next;
        }
    }
    tail.next = (list1 !== null) ? list1 : list2;
    // if (listA !== null) {
    //     tail.next = listA;
    // } else {
    //     tail.next = listB;
    // }
    return newHead.next;
}

function getMid(head) {

    let midHead = null;
    let slow = head;
    let fast = head
    while (fast !== null && fast.next !== null) {
        midHead = slow;
        slow = slow.next;
        fast = fast.next.next;
    }
    //disconnect, split them into 2 lists
    let secondHalf = midHead.next;
    midHead.next = null;
    return secondHalf;
}




// Solution2:
// // count how many nodes in the linked list
// function getCount(head) {
//     let count = 0;
//     while (head !== null) {
//         head = head.next;
//         count++;
//     }
//     return count;
// }


// @lc code=end
