class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_traverse = True
        for i in range(len(nums)):
            z = i + 1
            while list_traverse:
                total = nums[i] + nums[z]
                if total == target:
                    return [i, z]
                    list_traverse = False
                    break
                z += 1
                if z == len(nums):
                    break
