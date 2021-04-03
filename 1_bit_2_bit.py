#https://leetcode.com/problems/1-bit-and-2-bit-characters/submissions/
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if 1 in bits: 
            first_one_index = bits.index(1)
            del bits[:first_one_index]
        while(len(bits)>0):
            if len(bits)==2:
                if bits[0]==1:
                    return False
                else:
                    return True
            elif len(bits)==1:
                return True
            if bits[0]==1:
                bits.pop(0)
                bits.pop(0)
                # print(bits)
            else:
                bits.pop(0)
                # print(bits)
