class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # helper function to check vowels
        def check_vowels(ch):
            if ch in 'aeiou':
                return True
            else:
                return False

        sub_s = s[0:k]
        vowel_count = 0
        for ch in sub_s:
            if check_vowels(ch):
                vowel_count += 1
        print(vowel_count)
        max_v = vowel_count

        for i in range(k, len(s)):
            if check_vowels(s[i-k]):
                vowel_count -= 1
            if check_vowels(s[i]):
                vowel_count += 1
            
            max_v = max(max_v, vowel_count)
        
        return max_v