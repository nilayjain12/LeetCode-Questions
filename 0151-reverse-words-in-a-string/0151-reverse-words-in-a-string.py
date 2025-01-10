class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split()
        print(list_s)
        
        rev_list_s = list_s[::-1]
        print(rev_list_s)

        new_s = " ".join(rev_list_s)
        print(new_s)

        return new_s