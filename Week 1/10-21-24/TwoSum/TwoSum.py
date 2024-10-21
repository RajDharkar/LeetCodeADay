class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        used = {}
        for i in range(0, len(nums)):
            if (target - nums[i]) in used.keys():
                return i, used[target - nums[i]]
            used[nums[i]] = i
        