class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        prefix= ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return prefix 
            prefix += strs[0][i]
        return prefix
        '''
        strs.sort()

        start=strs[0]
        end=strs[-1]
        res=""

        for i in range(min(len(start), len(end))):
            if start[i] == end[i]:
                res += start[i]
            else:
                break 
        return res



        
        