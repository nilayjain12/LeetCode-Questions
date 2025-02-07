class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading/trailing spaces
        
        if not s:  # Base case: empty string
            return 0

        str_num = ""
        sign = 1  # Default positive sign
        i = 0

        # Handling optional sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Extract numeric part
        while i < len(s) and s[i].isdigit():
            str_num += s[i]
            i += 1

        if not str_num:  # No valid digits found
            return 0

        actual_num = sign * int(str_num)

        # Clamping to 32-bit integer range
        int_min, int_max = -2**31, 2**31 - 1
        if actual_num < int_min:
            return int_min
        elif actual_num > int_max:
            return int_max
        else:
            return actual_num