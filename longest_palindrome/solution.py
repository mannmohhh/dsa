class Solution:
    def longestPalindrome(self, s):
        max_pali = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                temp = s[i:j]
                if temp == temp[::-1]:
                    if len(temp) > len(max_pali):
                        max_pali = temp
        return max_pali
