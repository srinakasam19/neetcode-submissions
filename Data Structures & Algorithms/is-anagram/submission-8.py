class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        if sorted(s) == sorted(t):
            return True 
        return False
    '''
        if len(s) != len(t):
            return False
        arr=[0]*266
        for i in range(len(s)):
            arr[ord(s[i])] +=1 
            arr[ord(t[i])] -=1 
        for num in arr:
            if num != 0:
                return False 
        return True      
    
    '''
        if len(s) != len(t):
            return False
        d1={}
        d2={}

        for i in range(len(t)):
            d1[s[i]]= d1.get(s[i],0) + 1 
            d2[t[i]] = d2.get(t[i],0)+1

        return d1 == d2
        '''
        
        