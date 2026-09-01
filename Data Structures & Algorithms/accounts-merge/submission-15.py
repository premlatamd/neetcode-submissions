class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x,parent):
            if parent[x] != x:
                parent[x] = find(parent[x], parent)
            return parent[x]

        def union(a,b,parent):
            pa=find(a,parent)
            pb=find(b,parent)
            if pa!=pb:
                parent[pb]=pa
        d={}
        parent=[i for i in range(len(accounts))]
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email not in d:
                    d[email] = i
                else:
                    union(i, d[email], parent)

        d1={}
        for email, acc in d.items():
            root = find(acc,parent)
            if root not in d1:
                d1[root]=set()
            d1[root].add(email)
        
        ans = []
        for root, emails in d1.items():
            ans.append([accounts[root][0]] + sorted(emails))
        return ans
