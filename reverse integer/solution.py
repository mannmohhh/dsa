class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Check for overflow before it happens
            if res > (INT_MAX - pop) // 10:
                return 0
            res = res * 10 + pop
        
        return sign * res
