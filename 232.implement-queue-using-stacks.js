/*
 * @lc app=leetcode id=232 lang=javascript
 *
 * [232] Implement Queue using Stacks
 */

// @lc code=start

var MyQueue = function () {
    this.pushStack = [];
    this.popStack = [];
};

/**
 * @param {number} x
 * @return {void}
 */
// how to have the new pushed item be in the front
MyQueue.prototype.push = function (x) {
    this.pushStack.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function () {
    if (!this.popStack.length) {
        while (this.pushStack.length) {
            this.popStack.push(this.pushStack.pop());
        }
    }

    return this.popStack.pop();
};

MyQueue.prototype.pop = function () {
    return this.stack.pop();

};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function () {
    return this.stack[this.stack.length - 1];
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function () {
    return this.stack.length === 0
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
// @lc code=end
