class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            pop_num = nums.pop()
            print(pop_num)
            nums.insert(0, pop_num)