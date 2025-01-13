class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j, res = 0, 0, []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        res.extend(nums1[i:])
        res.extend(nums2[j:])
        print(res)
        return median(res)