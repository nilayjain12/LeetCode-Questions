class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        Approach - 1:
        '''
        # If the lengths of the two words are different, they cannot be close
        if len(word1)!=len(word2):
            return False
        
        # Count the frequency of each character
        charFreq1 = {c:0 for c in word1}
        charFreq2 = {c:0 for c in word2}
        for c in word1:
            charFreq1[c] += 1
        for c in word2:
            charFreq2[c] += 1
        
        # Check two conditions for words to be close:
        # 1. Both words must contain the same set of unique characters.
        # 2. The sorted frequency counts of the characters in both words must match.
        return charFreq1.keys() == charFreq2.keys() and sorted(charFreq1.values()) == sorted(charFreq2.values())
        
        '''
        Approach - 2
        '''
        # if (len(word1) != len(word2)) or (set(word1) != set(word2)):
        #     return False
        # fr1 = Counter(word1)
        # print(fr1)

        # fr2 = Counter(word2)
        # print(fr2)

        # if sorted(fr1.values()) != sorted(fr2.values()):
        #     return False
        # return True