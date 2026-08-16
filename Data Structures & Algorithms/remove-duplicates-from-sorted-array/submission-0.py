class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            if nums[i] not in l:
                l.append(nums[i])
        for i in range(len(l)):
            nums[i] = l[i]
        return len(l)

        