class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph = ""
        for c in s:
            if c.isalnum():
                alph+=c.lower()
        i,j = 0, len(alph)-1
        while(i<j):
            if(alph[i] != alph[j]):
                return False
            i+=1
            j-=1
        
        return True