# coding: utf-8

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in xrange(0, len(nums) - 1):
            target = nums[i]
            x = i + 1
            y = len(nums) - 1
            while x < y:
                midres = nums[x] + nums[y]
                if midres == -target:
                    tmp = (target, nums[x], nums[y])
                    if tmp not in result:
                        result.append(tmp)
                    x += 1
                    y -= 1
                elif midres > -target:
                    y -= 1
                else:
                    x += 1
        return result


# print Solution().threeSum([-1, 0, 1, 2, -1, -4, 3])