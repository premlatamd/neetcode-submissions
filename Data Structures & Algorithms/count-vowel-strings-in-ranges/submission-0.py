class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel=["a","e","i","o","u"]
        ans=[]
        for s,e in queries:
            count=0
            for i in range(s,e+1):
                if words[i][0] in vowel and words[i][-1] in vowel:
                    count+=1
            ans.append(count)
        print(ans)
        return ans
        