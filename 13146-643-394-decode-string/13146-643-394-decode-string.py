class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ''
        curr_num = 0

        for ch in s:
            if ch == '[':
                stack.append(curr_string)
                stack.append(curr_num)
                curr_string = ''
                curr_num = 0
            elif ch == ']':
                num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + num*curr_string
            elif ch.isdigit():
                curr_num = 10*curr_num + int(ch)
            else:
                curr_string += ch
        
        return curr_string