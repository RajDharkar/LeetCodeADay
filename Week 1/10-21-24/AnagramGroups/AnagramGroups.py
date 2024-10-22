class Solution:
    def groupAnagrams(self, strs):
        mp = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in mp:
                mp[sorted_string].append(string)
            else:
                mp[sorted_string] = [string]
        return mp.values()
