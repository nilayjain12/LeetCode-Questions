class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        '''
        Approach-1:
        '''
        set_1, set_2 = set(nums1), set(nums2)

        return [list(set_1 - set_2), list(set_2 - (set_1 & set_2))]

        '''
        Approach - 2
        '''
                
        # dict_nums1, dict_nums2 = {}, {}
        # list_1, list_2 = [], []
        # for num in nums1:
        #     if num not in dict_nums1:
        #         dict_nums1[num] = 1
        # for num in nums2:
        #     if num not in dict_nums2:
        #         dict_nums2[num] = 1

        # for key in dict_nums1:
        #     if key not in dict_nums2:
        #         list_1.append(key)
        # for key in dict_nums2:
        #     if key not in dict_nums1:
        #         list_2.append(key)
        
        # return [list_1, list_2]