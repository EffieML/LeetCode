/*
 * @lc app=leetcode id=205 lang=javascript
 *
 * [205] Isomorphic Strings
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

// egg
// adf
// time O(n), space O(1)
// "badc"  "baba" has to check both map, cant only do one
var isIsomorphic = function (s, t) {
    if (s.length !== t.length) return false;

    let sMap = {};
    let tMap = {};
    for (let i = 0; i < s.length; i++) {
        let sChar = s[i];  //e
        let tChar = t[i];  //f

        if (sMap[sChar] === undefined) {
            sMap[sChar] = tChar;
        }
        if (tMap[tChar] === undefined) {
            tMap[tChar] = sChar;
        }
        if (sMap[sChar] !== tChar || tMap[tChar] !== sChar) return false;
    }
    return true;
};

// // egg
// // adf
// // need to consider each word postition is unique, use i+1, instead of value+1
// var isIsomorphic = function (s, t) {
//     if (s.length !== t.length) return false;

//     let sArr = new Array(128).fill(0);
//     let tArr = new Array(128).fill(0);

//     for (let i = 0; i < s.length; i++) {
//         let sIdx = s.charCodeAt(i);
//         let tIdx = t.charCodeAt(i);
//         if (sArr[sIdx] !== tArr[tIdx]) return false;

//         sArr[sIdx] = i + 1;
//         tArr[tIdx] = i + 1;
//     }
//     return true;
// };



// @lc code=end
