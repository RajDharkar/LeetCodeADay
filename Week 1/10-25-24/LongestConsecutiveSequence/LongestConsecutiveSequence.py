from sortedcontainers import SortedList, SortedSet, SortedDict 

class Solution(object):
    def longestConsecutive(self, nums):
        nums = sorted(nums)
        prev = 1e10
        current_max = 0
        current_count = 0
        for num in nums:
            if num == prev + 1:
                current_count+=1
                current_max = max(current_max, current_count)
            else:
                prev = num
                current_count = 0
        return current_max