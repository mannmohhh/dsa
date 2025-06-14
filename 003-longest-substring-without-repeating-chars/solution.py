class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                t = s[i:j+1]
                if len(set(t)) == len(t):
                    if len(t) > res:
                        res = len(t)
        return res
