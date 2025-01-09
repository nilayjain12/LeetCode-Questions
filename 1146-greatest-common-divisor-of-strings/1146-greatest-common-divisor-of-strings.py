class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        temp_s = str2 if len(str2) <= len(str1) else str1

        def check_for_equal(string_to_pass, other_string, temp_s):
            if string_to_pass == temp_s * (len(string_to_pass) // len(temp_s)) and other_string == temp_s * (len(other_string) // len(temp_s)):
                return True

        while len(temp_s) > 0:
            string_to_pass = str2 if len(str2) > len(str1) else str1
            other_string = str1 if len(str2) > len(str1) else str2
            if check_for_equal(string_to_pass, other_string, temp_s):
                return temp_s
            else:
                temp_s = temp_s[:-1]

        return ""