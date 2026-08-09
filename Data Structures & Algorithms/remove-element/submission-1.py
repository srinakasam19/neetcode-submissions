class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        while val in nums:
            nums.remove(val)
        return len(nums)
        '''
        l=[]
        for i in nums:
            if i != val:
                l.append(i)
        for i in range(len(l)):
            nums[i] = l[i]
        return len(l)
        