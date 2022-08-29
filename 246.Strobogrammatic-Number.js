var isStrobogrammatic = function (num) {
    var n = num.length;
    for (let i = 0, j = n - 1; i <= j; i++, j--) {
        var c = num[i] + num[j];
        if (c != '00' && c != '11' && c != '88' && c != '69' && c != '96') {
            return false;
        }
    }
    return true;
};

// not the best, need try hash-map
