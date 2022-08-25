/*
 * @lc app=leetcode id=225 lang=javascript
 *
 * [225] Implement Stack using Queues
 */

// @lc code=start

var MyStack = function () {
    this.queue = new Array;
    this.length = 0;
};

/**
 * @param {number} x
 * @return {void}
 */
// time: O(n), space: O(1)
// queue will always add new item to the end, how to make this new added to the front?
// once add it, move all previous items to the end of it.
MyStack.prototype.push = function (x) {
    this.queue.push(x);
    for (let i = 0; i < this.length; i++) {
        let temp = this.queue.shift();
        this.queue.push(temp);
    }
    this.length++;
    return this.queue;
};



/**
 * @return {number}
 */
// time: O(1), space: O(1)
MyStack.prototype.pop = function () {
    this.length--;
    return this.queue.shift()
};

/**
 * @return {number}
 */
// time: O(1), space: O(1)
MyStack.prototype.top = function () {
    return this.queue[0];
};

/**
 * @return {boolean}
 */
// time: O(1), space: O(1)
MyStack.prototype.empty = function () {
    return !this.queue.length;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
// @lc code=end
