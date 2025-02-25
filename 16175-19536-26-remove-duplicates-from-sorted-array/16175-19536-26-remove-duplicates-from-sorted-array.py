class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dict_nums = {}

        for i in nums:
            if i not in dict_nums:
                dict_nums[i] = 1
            else:
                pass
        
        list_nums = [key for key in dict_nums]

        nums[:] = list_nums
        return len(nums)