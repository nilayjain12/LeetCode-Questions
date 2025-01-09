class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        Approach 1:
        '''
        # out_s = ''

        # # case 1, 2, 3
        # if len(word1) == len(word2):
        #     for i in range(len(word1)):
        #         out_s += word1[i]
        #         out_s += word2[i]
        # elif len(word1) < len(word2):
        #     for i in range(len(word1)):
        #         out_s += word1[i]
        #         out_s += word2[i]
        # else:
        #     for i in range(len(word2)):
        #         out_s += word1[i]
        #         out_s += word2[i]

        # if i+1 < len(word1):
        #     out_s += word1[i+1:]
        # elif i+1 < len(word2):
        #     out_s += word2[i+1:]
        
        # return out_s

        '''
        Approach 2:
        '''
        # out_s = ''

        # for i, j in enumerate(zip(word1, word2)):
        #     out_s += j[0] + j[1]

        # out_s += word2[i+1:]
        # out_s += word1[i+1:]

        # return out_s

        '''
        Approach 3:
        '''
        i,j=0,0
        str=[]
        while i <len(word1) and j <len(word2):
            
            str.append(word1[i])
            str.append(word2[j])
            i+=1
            j+=1

        str.append(word1[i:])
        str.append(word2[j:])
        return "".join(str)