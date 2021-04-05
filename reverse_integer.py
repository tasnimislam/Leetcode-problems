#https://leetcode.com/problems/reverse-integer/submissions/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r_int = str(abs(x))[::-1]
        if x<0:
            r_int = "-" + r_int
        #print(int(r_int))
        
        if int(r_int) < -2**31 or int(r_int) > 2**31-1:
			      r_int = 0
        return int(r_int)
