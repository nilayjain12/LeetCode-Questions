class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        Approach 1:
        '''
        s_list = [ch for ch in s]
        print(s_list)
        vowels = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
        i, j = 0, len(s)-1

        while i < j:
            # check if both i, j are vowels
            if s_list[i] in vowels and s_list[j] in vowels:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
            # check if j is not vowel
            elif s_list[i] in vowels and s_list[j] not in vowels:
                j -= 1
            # check if i is not vowel
            elif s_list[j] in vowels and s_list[i] not in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        
        return "".join(s_list)


