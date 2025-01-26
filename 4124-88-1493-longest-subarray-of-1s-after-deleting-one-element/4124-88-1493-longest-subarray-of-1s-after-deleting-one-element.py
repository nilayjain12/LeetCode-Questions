class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zerocount, max_val = 0, 0, 0

        for right in range(0, len(nums)):
            if nums[right] == 0:
                zerocount += 1
            
            while zerocount > 1:
                if nums[left] == 0:
                    zerocount -= 1
                left += 1
            
            max_val = max(max_val, right - left + 1 - zerocount)
        
        if max_val == len(nums):
            return max_val - 1
        else:
            return max_val