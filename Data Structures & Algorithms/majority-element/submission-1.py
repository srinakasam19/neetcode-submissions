class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        d={}
        for i in nums:
            if i not in d:
                d[i] = 1
            else :
                d[i] += 1 
        for key in d:
            if d[key] > len(nums) // 2 :
                return key
        '''
        nums.sort()
        return nums[len(nums) // 2]



        