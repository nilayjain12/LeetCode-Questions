class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize new arr
        res = [1] * len(nums)
        print(res)

        left_prod = 1
        # left iteration
        for i in range(0, len(nums)):
            res[i] *= left_prod
            left_prod *= nums[i]
        print(res)

        right_prod = 1
        # right iteration
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right_prod
            right_prod *= nums[i]
        print(res)

        return res