class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        Approach 1:
            1. add zeroes to start and end.
            2. loop through flowerbed, start i from 1.
            3. check if at pos i-1 and i+1 are are 0.
                i) if yes, then add 1 at i position and subtract 1 from n.
            4. check if n == 0, then return true else flase.
        '''
        for i in range(len(flowerbed)):
            left = (i == 0) or (flowerbed[i-1] == 0)
            right = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0
