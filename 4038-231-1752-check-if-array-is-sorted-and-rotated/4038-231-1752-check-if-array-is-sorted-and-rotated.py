from collections import deque
class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = nums.copy()
        if nums.sort() == nums:
            return True
        else:
            for i in range(len(arr)):
                arr.append(arr.pop(0))
                if arr == nums:
                    return True
        
        return False



'''
if the nums == nums.sort(): return TRUE
else:
     in a loop reverse rotate the nums by 1:
         check at each rotation if rotated_nums == nums.sort():
             return TRUE

     return FALSE
'''