class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_freq = {}
        for num in arr:
            if num not in dict_freq:
                dict_freq[num] = 1
            else:
                dict_freq[num] += 1
        
        set_freq = list()
        for key, val in dict_freq.items():
            set_freq.append(val)
        
        return (len(set(set_freq)) == len(set_freq))