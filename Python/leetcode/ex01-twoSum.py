#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, nums, target):
        i = 0
        print(len(nums))
        while i < len(nums):
            j = i + 1
            if nums[i] > target:
                i = i + 1
                continue
            while j < len(nums):
                if nums[j] > target:
                    j = j + 1
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
                j = j + 1
            i = i + 1


s = Solution()
res = s.twoSum([3, 2, 4], 6)
print(res)