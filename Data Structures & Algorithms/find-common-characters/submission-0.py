from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common=Counter(words[0])
        for i in words[1:]:
            common &= Counter(i)

        print(common)
        ans=[]
        for key,i in common.items():
            ans.extend([key] * i)
        print(ans)
        return ans


        

        