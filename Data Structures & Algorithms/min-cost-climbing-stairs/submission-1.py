class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a=cost[0]
        if len(cost)==1:
            return cost[0]
        b=cost[1]
        if len(cost)==2:
            return min(a,b)

        for i in range(2,len(cost)):
            c=cost[i]+min(a,b)
            a=b
            b=c

        return min(a,b)
        
        """n=len(cost)
        ans1=0
        ans2=0
        for i in range(0,n,2):
            ans1+=cost[i]
        
        for i in range(1,n,2):
            ans2+=cost[i]
        ans=min(ans1,ans2)

        i=0
        p=0
        while i<n-1:
            if cost[i]<cost[i+1]:
                p+=cost[i]
            elif cost[i]>cost[i+1]:
                p+=cost[i+1]
            else:
                p+=cost[i]
                i+=2
                
                

            i+=1



        return ans"""



        
        