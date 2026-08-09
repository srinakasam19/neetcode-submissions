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
        '''
        nums.sort()
        return nums[len(nums) // 2]
        '''
        candidate = 0 
        count =0 
        for num in nums:
            if count == 0:
                candidate = num 
            if candidate == num:
                count += 1
            else:
                count -= 1 
        return candidate



        