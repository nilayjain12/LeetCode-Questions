class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, c = 0, 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                c += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return len(s) == c