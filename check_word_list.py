#https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3681/

class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        vowel = ['a', 'e', 'i', 'o', 'u']
        new_quer_list = []
        for quer in queries:
            for word in wordlist:
                if quer==word:
                    new_quer_list.append(quer)
                else:
                    continue
                    
        return new_quer_list
                    
                        
                            
                        
                            
