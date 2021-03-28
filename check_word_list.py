#https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3681/

class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        vowel = ['a', 'e', 'i', 'o', 'u']
        quer_list_ind = 0
        new_word_list = []
        while(quer_list_ind<len(queries)):
            word_list_ind = 0
            new_word = ""
            while(word_list_ind<len(words)):
                q_ind = 0
                w_ind = 0
                while(q_ind<len(queries[quer_list_ind]) and w_ind<len(word[word_list_ind])):
                     if (queries[quer_list_ind][q_ind].lower() not in vowel) and queries[quer_list_ind][q_ind].lower()!= wordlist[word_list_ind][w_ind].lower():
                            word_list_ind +=1
                            break
            new_word_list.append(new_word)
                        
                            
