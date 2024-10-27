class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        ret = (r - l) * min(height[r], height[l])
        while l < r:
            print(ret)        
            ret = max(ret, (r - l) * min(height[r], height[l]))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return ret

                    