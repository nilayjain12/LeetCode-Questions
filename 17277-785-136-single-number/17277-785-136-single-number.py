class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        nums.sort()

        i, j = 0, 1
        while i < len(nums):
            if j >= len(nums):
                return nums[i]
            
            if nums[i] == nums[j]:
                i += 2
                j += 2
            else:
                return nums[i]
