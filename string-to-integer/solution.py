class Solution(object):
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        INT_BOUND = INT_MAX // 10  # 214748364
        
        index = 0
        n = len(s)
        
        # Skip leading whitespace
        while index < n and s[index] == ' ':
            index += 1
            
        if index == n:
            return 0
            
        sign = 1
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        result = 0
        while index < n and s[index].isdigit():
            digit = int(s[index])
            if result > INT_BOUND or (result == INT_BOUND and digit > (7 if sign == 1 else 8)):
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            index += 1
            
        return sign * result
