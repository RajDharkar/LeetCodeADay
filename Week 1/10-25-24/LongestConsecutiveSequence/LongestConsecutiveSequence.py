class Solution(object):
    def longestConsecutive(self, nums):
        nums = sorted(nums)
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        prev = 1e10
        current_max = 0
        current_count = 0
        for num in nums:
            if num == prev + 1 or prev == 1e10:
                current_count+=1
                current_max = max(current_max, current_count)
                prev = num
            else:
                prev = num
                current_count = 1
        return current_max