class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        s=set(nums)
        if len(nums) != len(s):
            return True 
        return False
        '''
        '''
        for i in nums:
            if nums.count(i) > 1:
                return True
        return False
        '''
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                return True 
        return False



        