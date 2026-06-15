class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.front1=-1
        self.rear1=-1
        self.front2=-1
        self.rear2=-1
        

    def push(self, x: int) -> None:
        (self.stack1).append(x)
        """if self.rear1==-1 and self.front1==-1:
            self.rear1+=1
        #if len(self.stack1)>self.front1:
        self.front1+=1
        (self.stack1).append(x)"""
        

    def pop(self) -> int:
        while(self.stack1)!=[]:
           x=(self.stack1).pop()
           (self.stack2).append(x)

        y=(self.stack2).pop()
        while(self.stack2)!=[]:
           x1=(self.stack2).pop()
           (self.stack1).append(x1)


        return y
        """while (self.stack1)!=[]:
            x=(self.stack1).pop()
            if self.rear2==-1 and self.front2==-1:
                self.rear2+=1   
            
            self.front2+=1
            (self.stack2).append(x)
        print("hola",(self.stack2),self.front2,(self.stack2)[self.front2])
        y=(self.stack2)[self.front2]
        (self.front2)-=1
        while (self.stack2)!=[]:
            x2=(self.stack2).pop()
            if self.rear1==-1 and self.front1==-1:
                self.rear1+=1   
            if len(self.stack1)>self.front1: 
                self.front1+=1
                (self.stack1).append(x2)
        return y
        """
        

    def peek(self) -> int:
        x=(self.stack1)[0]
        return x
        

    def empty(self) -> bool:
        if self.stack1==[]:
            return True
        return False
        """if self.rear1==-1 and self.front1==-1 :
            return True
        return False"""
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()