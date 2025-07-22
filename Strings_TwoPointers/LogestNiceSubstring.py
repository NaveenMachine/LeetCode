# Nice substring: abAB

class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return "" # boundary condition 
        ss = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in ss: 
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key=len)
        return s
