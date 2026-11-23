class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1={}
        word2={}
        
        for n in s:

            word1[n]=word1.get(n, 0)+1
        
        for c in t:
            word2[c]=word2.get(c, 0)+1
        
        if(word1 == word2):
            return True
        return False