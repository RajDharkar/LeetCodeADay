class Solution(object):
    def dailyTemperatures(self, temperatures):
        results = [0] * len(temperatures)
        nosol = []
        for i in range(len(temperatures)):   
            while len(nosol) != 0 and temperatures[i] > temperatures[nosol[len(nosol) - 1]]:
                top = nosol.pop()
                results[top] = i - top
            nosol.append(i)
        return results