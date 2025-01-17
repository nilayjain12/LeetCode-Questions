class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # initalizing first and second minimum
        # initialize it with infinity

        first_min = float('inf')
        second_min = float('inf')

        # iterate through numbers to find first and second minimum value
        for num in nums:
            
            # if num <= first then make first as the num
            if num <= first_min:
                first_min = num
            # similarly for second minimum
            elif num <= second_min:
                second_min = num
            # once both first and second minimums are found we return True
            else:
                return True
        
        # if loop ends then return false
        return False