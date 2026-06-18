class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        a=[]
        p=sorted(people)
       
        boat=0
        i=0
        j=len(people)-1
        if people==[]:
            return 0
             
        while i<=j:
              
            if p[i]+p[j]<=limit:
                i+=1   
            j-=1 
            boat+=1                
           
        print(boat)
        return boat

        

              


                           



        """ while j<=n:
            m=limit-people[j] 
            if m not in s and m in people[j+1:]:
                s.append(people[j])
                j+=1
            else:
                a.append([m,people[j]])
                s.remove(m)
                s.remove(people[j])
                i+=1
                j=i

        """