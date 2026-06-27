class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        
        def fun(asteroids: List[int]) -> List[int]:
            l=0
            n=len(asteroids)
            a=[]
            if asteroids==[]:
                return asteroids
            
            if len(asteroids)==1:
                return asteroids
            for i in asteroids:
                while len(a)>1:
                    x1=a[-1]
                    x2=a[-2]
                    if x2>0 and x1<0:
                        a=fun(a)
                    else:
                        break
                        
                if (a==[] or i>0) or (a==[] and i<0):
                    a.append(i)

                elif i<0:
                    x=a[-1]
                    if x>0:
                        if abs(x)<abs(i):
                            a.pop()
                        elif abs(x)==abs(i):
                            a.pop()
                            continue
                        else:
                            continue

                    a.append(i)
            return a

        m=fun(asteroids)
       
        while len(m)>1:
           
            x1=m[-1]
            x2=m[-2]
            if x2>0 and x1<0:
                m=fun(m)
            else:
                break
        return m
    






        


        

        