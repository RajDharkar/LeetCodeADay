from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        return [num for num, _ in counter.most_common(k)]