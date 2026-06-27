class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a=[]
        for i in bills:
            
            if i==10:
                if 5  not in a:
                    return False
                a.remove(5)

            elif i==20:
                if (5 in a and 10 in a):
                    a.remove(10)
                    a.remove(5)
               
                elif (5 not in a):
                    return False
                elif 10 not in a:
                    try:
                        a.remove(5)
                        a.remove(5)
                        a.remove(5)

                    except:
                        return False
                

            a.append(i)

        return True