class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=strs[0]
        c=0
        for i in strs[1:len(strs)]:
            for j in range(len(l)+1):
                if l=="":
                    return l
                if l not in i:
                    l=l[:len(l)-1]

        return l
            