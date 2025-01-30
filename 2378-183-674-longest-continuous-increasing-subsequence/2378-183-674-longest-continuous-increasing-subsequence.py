class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_val = 1
        i, j = 0, 1
        final_max = 0


        while j < len(nums):
            if nums[j] > nums[j-1]:
                max_val += 1
                j += 1
            else:
                final_max = max(final_max, max_val)
                max_val = 1
                i = j
                j += 1
        
        return final_max if final_max > max_val else max_val