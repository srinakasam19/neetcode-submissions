class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        l=[]
        s=s.lower()
        for i in s:
            if i.isalnum():
                l.append(i)
        if l== l[::-1]:
            return True 
        return False
        '''
        s=s.lower()
        i=0
        j=len(s)-1
        while(i<j):
            while i<j and not s[i].isalnum():
                i += 1 
            while i<j and not s[j].isalnum():
                j -= 1 
            if s[i] != s[j]:
                return False 

            i += 1 
            j -= 1 
        else:
            return True 



