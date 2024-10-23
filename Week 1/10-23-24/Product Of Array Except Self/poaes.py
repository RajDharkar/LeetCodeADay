class Solution(object):
    def productExceptSelf(self, nums):
        answer = []
        product = 1
        zero = False
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount+=1
        if zeroCount > 1:
            answer = [0] * len(nums)
            return answer
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero = True
        for num in nums:
            if num == 0:
                answer.append(product)
            else:
                if zero:
                    answer.append(0)
                else:
                    answer.append(product / num)
        return answer