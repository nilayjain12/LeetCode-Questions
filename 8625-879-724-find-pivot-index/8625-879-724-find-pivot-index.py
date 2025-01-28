class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 1:
            return 0
        
        left_sum, right_sum = 0, sum(nums[1:])

        for i in range(0, len(nums)-1):
            # check the left and right sum
            if left_sum == right_sum:
                return i
            else:
                left_sum += nums[i]
                right_sum -= nums[i+1]
        
        # check for the right case
        right_sum, left_sum = 0, sum(nums[0:len(nums)-1])
        if left_sum == right_sum:
            return len(nums)-1

        return -1
