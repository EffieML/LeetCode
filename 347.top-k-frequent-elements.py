#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# @lc code=start
# from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # nums = [1, 1, 1, 2, 2, 100]
        count = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]

        for num, count in count.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    # print(res)
                    return res

        # count = {}
        # freq = [[] for i in range(len(nums)+1)]
        # print(freq)
        # for num in nums:
        #     count[num] = 1+ count.get(n,0)
        # for num in nums:
        #     if num in count:
        #         count[num] += 1
        #     else:
        #         count[num] = 1
        # for num, count in count.items():
        #     freq[count].append(num)
        # res = []
        # for i in range(len(freq)-1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res
# bucket sort time O(n)
# @lc code=end
# nums = [1, 1, 2, 3, 3]
# k = 2

# test = Solution()
# test.topKFrequent(nums, k)
