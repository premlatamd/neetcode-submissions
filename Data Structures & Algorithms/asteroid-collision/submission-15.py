class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        
        def fun(asteroids: List[int]) -> List[int]:
            l=0
            n=len(asteroids)
            a=[]
            if asteroids==[]:
                return asteroids
            """if asteroids!=[]:
                a.append(asteroids[0])"""
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
    






        """ r=1
        while r<n:
           

            if abs(a[-1])>abs(asteroids[r]):
                if (a[-1]>0 and asteroids[r]<0):
                    continue
                
                    a.append(asteroids[r])

            elif abs(a[-1])<abs(asteroids[r]):
                if (a[-1]>0 and asteroids[r]<0) or (a[-1]<0 and asteroids[r]>0):
                    a.pop()
                
                a.append(asteroids[r])

            else:
                if a[-1]!=asteroids[r]:
                    a.pop()
                else:
                    a.append(asteroids[r])

            r+=1

        if len(a)>1:
            if abs(a[0])>abs(a[1]):
                a.pop()
            

        return a"""




        """m=a[-1]+asteroids[r]
            print("ho;a",a[-1])
            if abs(a[-1]) < abs(asteroids[r]):
                if m > asteroids[r]:
                    a.append(asteroids[r])

                else:
                    a.remove(a[-1])
                    a.append(asteroids[r])

                

            elif abs(a[-1]) > abs(asteroids[r]):
                if m > a[-1]:
                    a.append(asteroids[r])

            else:
                if m==0:
                    a.remove(a[-1])
                else:
                    a.append(asteroids[r])

                
        return a"""






            


        

        