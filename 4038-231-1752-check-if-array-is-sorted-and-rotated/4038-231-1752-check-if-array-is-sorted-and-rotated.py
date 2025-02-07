from collections import deque
class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = nums.copy()
        sorted_nums.sort()
        # find all positions of the first element of nums in the sorted list
        possible_rotations = [i for i, x in enumerate(sorted_nums) if x == nums[0]]
        
        for num_rotation in possible_rotations:
            rotations = (len(nums) - num_rotation) % len(nums)
            
            sorted_numsQ = deque(sorted_nums)
            print("Nums =", nums)
            print("Sorted Nums List =", sorted_nums)
            print("Sorted Nums Queue =", sorted_numsQ, "type =", type(sorted_numsQ))
            print("Testing Position =", num_rotation)
            print("Rotations to perform =", rotations)
            
            # perform the right rotations on sorted_numsQ
            for i in range(rotations):
                sorted_numsQ.appendleft(sorted_numsQ.pop())
            
            print("Rotated Queue =", sorted_numsQ)
            print("Rotated List =", list(sorted_numsQ))
            
            # compare the rotated list with the original nums and return True/False
            if list(sorted_numsQ) == nums:
                return True
        return False