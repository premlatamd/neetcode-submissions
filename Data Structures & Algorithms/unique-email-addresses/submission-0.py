class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s=set()
        for email in emails:
            local=email.split("@")
            local[0]="".join(local[0].split("."))
            ans=local[0].split("+")
            ans[0]+=local[1]
            s.add(ans[0])
        print(s)

        return len(s)
        