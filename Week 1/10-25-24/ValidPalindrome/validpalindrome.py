class Solution(object):
    def isPalindrome(self, s):
        r = len(s) - 1
        l = 0
        while l < r:
            if s[i].isalpha() or s[i].is_numeric():
                if s[l] != s[r]:
                    return False
            l+=1
            r-=1
        