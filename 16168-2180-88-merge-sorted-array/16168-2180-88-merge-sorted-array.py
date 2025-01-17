class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged_arr = []

        # append the nums from nums1 from 0 till m
        for i in range(0, m):
            merged_arr.append(nums1[i])
        
        # append the nums from nums2 from 0 till n
        for i in range(0, n):
            merged_arr.append(nums2[i])
        
        # sort the array
        merged_arr.sort()
        print(merged_arr)

        # making in-place assignment to nums1
        nums1[:] = merged_arr