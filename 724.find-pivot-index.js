/*
 * @lc app=leetcode id=724 lang=javascript
 *
 * [724] Find Pivot Index
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function (nums) {
    let totalSum = 0;
    let leftSum = 0;

    for (let i = 0; i < nums.length; i++) {
        totalSum += nums[i];
    }

    for (let j = 0; j < nums.length; j++) {
        if (leftSum === totalSum - leftSum - nums[j]) return j;
        leftSum += nums[j];
    }

    return -1;
};

// time complexity O(n) 2n; space O(1)

// @lc code=end
