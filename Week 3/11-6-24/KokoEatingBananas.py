class Solution(object):
    def minEatingSpeed(self, piles, h):
        def check(val):
            hours_taken = 0
            for pile in piles:
                hours_taken += (pile + val - 1)//val
            return hours_taken <= h
        def binarysearch(lo, hi):
            hi+=1
            while lo < hi:
                mid = (lo + hi) // 2
                if check(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        return binarysearch(0, sum(piles))

            break