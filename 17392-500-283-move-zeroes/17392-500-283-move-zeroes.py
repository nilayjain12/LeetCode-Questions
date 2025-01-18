class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        count = 0
        for num in nums:
            if num != 0:
                res.append(num)
            else:
                count += 1
        
        res.extend([0]*count)
        
        nums[:] = res