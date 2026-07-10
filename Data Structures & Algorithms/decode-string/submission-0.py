class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        for i in s:

            if i != ']':
                stack.append(i)

            else:
                curr=""

                # string nikalo
                while stack[-1] != '[':
                    curr = stack.pop() + curr

                # [ hatao
                stack.pop()


                # number nikalo
                num=""

                while stack and stack[-1].isdigit():
                    num = stack.pop() + num


                # repeat karke wapas daalo
                stack.append(int(num)*curr)


        return "".join(stack)