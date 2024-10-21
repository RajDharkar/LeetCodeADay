class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}

        for i in range(0, len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
        
        return s_dict == t_dict
    
    