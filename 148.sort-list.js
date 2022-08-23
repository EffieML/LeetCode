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

    let n = getCount(head);
    let start = head;

    let leftlist = head.slice(0, mid);
    let rightlist = head.slice(mid);

    let leftsort = sortList(leftlist);
    let rightsort = sortList(rightlist);
    console.log(head);
    return merge(leftsort, rightsort);
};

function merge(listA, listB) {
    let mergeList = [];
    let ai = 0;
    let bi = 0;
    // iterate through listA and listB, add the smaller one to the arr
    while (ai < listA.length || bi < listB.length) {
        if (ai === listA.length) {
            mergeList.push(listB[bi]);
            bi++;
        } else if (bi === listB.length) {
            mergeList.push(listA[ai]);
        } else if (listA[ai] < listB[bi]) {
            mergeList.push(listA[ai]);
            ai++;
        } else {
            mergeList.push(listB[bi]);
            bi++;
        }
    }
    return mergeList;
}

function getMid(ListNode, head) {
    let midPrev = null;
    while (head !== null && head.next !== null) {

    }
}

// count how many nodes in the linked list
function getCount(head) {
    let count = 0;
    while (head !== null) {
        head = head.next;
        count++;
    }
    return count;
}


arrA = [2, 4];
arrB = [1, 3]
merge(arrA, arrB);
// sortList(arr);
// @lc code=end
