class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        if len(nums) != len(set(nums)):
            return True
        return False
        '''
        d=[]
        for i in nums:
            if i not in d:
                d.append(i)
            else:
                return True 
        return False
            
        