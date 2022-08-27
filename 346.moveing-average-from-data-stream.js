
var MovingAverage = function (size) {
    this.size = size;
    this.queue = new Array;
};

/**
 * @param {number} val
 * @return {number}
 */
MovingAverage.prototype.next = function (val) {
    let list = this.queue;
    list.push(val);
    let sum = 0;

    if (list.length > this.size) {
        list.shift(list.length - this.size);
    }

    let i = 0;
    while (i < list.length) {
        sum += list[i]
        i++;
    }

    return sum / list.length;
}
