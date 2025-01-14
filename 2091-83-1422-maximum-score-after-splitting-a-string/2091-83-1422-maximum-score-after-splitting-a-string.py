class Solution:
    def maxScore(self, s: str) -> int:
        '''
        Approach1:
        1. Initialize 'res' array = []
        2. for j in range(1, len(array)
        3. left = [0:j], right = [j, len(array)]
            total = left.count(0) + right.count(1)
            res.append(total)
        '''
        res = []
        for j in range(1, len(s)):
            left, right = s[0:j], s[j:len(s)]
            res.append(left.count('0') + right.count('1'))
        
        return max(res)