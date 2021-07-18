
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtype = []
        cache = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in cache:
                rtype.append(cache[diff])
                rtype.append(i)
                break;
            else:
                cache[nums[i]] = i
        return rtype

obj = Solution()
positions = obj.twoSum([23, 4, 1, 50, 21, 8, 3], 26)
print(positions)
