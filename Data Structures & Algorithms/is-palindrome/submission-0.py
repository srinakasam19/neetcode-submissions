class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        s=s.lower()
        for i in s:
            if i.isalnum():
                l.append(i)
        if l== l[::-1]:
            return True 
        return False

        