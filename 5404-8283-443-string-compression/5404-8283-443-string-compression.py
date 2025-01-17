class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        temp_str = chars[0]     # a
        
        for i in range(1, len(chars)):
            # check if chars[i] in temp_str
            if chars[i] in temp_str:
                temp_str += chars[i]
            else:
                if len(temp_str) == 1:
                    res.append(temp_str[0])
                elif len(temp_str) >= 10:
                    res.append(temp_str[0])
                    for j in str(len(temp_str)):
                        res.append(str(j))
                else:
                    res.append(temp_str[0])
                    res.append(str(len(temp_str)))
                temp_str = ''
                temp_str += chars[i]
        
        # if temp string has something left
        if len(temp_str) > 0:
            if len(temp_str) == 1:
                    res.append(temp_str[0])
            elif len(temp_str) >= 10:
                res.append(temp_str[0])
                for j in str(len(temp_str)):
                    res.append(str(j))
            else:
                res.append(temp_str[0])
                res.append(str(len(temp_str)))

        # Update chars in-place and return the new length
        chars[:] = res  # Update the input list in-place
        print(res)
        return len(chars)
            
