class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_s = 0
        max_s = 0

        for i in range(len(nums)):
            # check if it's 1st elem of nums
            if i == 0:
                curr_s += nums[i]
                max_s = max(curr_s, max_s)
                continue
            
            # check if prev elem is larger than curr elem
            if nums[i] > nums[i-1]:
                curr_s += nums[i]
                max_s = max(curr_s, max_s)
            else:
                curr_s = nums[i]
                max_s = max(curr_s, max_s)
        
        return max_s