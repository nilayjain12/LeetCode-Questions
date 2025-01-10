class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        outarr = []
        max_num = max(candies)
        print(max_num)
        for i in range(len(candies)):
            
            if candies[i] + extraCandies >= max_num:
                outarr.append(True)
            else:
                outarr.append(False)
        
        return outarr