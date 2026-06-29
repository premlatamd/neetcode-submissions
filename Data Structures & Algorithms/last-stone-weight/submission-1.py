class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if stones==[]:
            return 0

        while len(stones)>1 :
            stones.sort()
            x=stones.pop()
            y=stones.pop()
            if x>y:
                x=x-y
                stones.append(x)
            elif x<y:
                y=y-x
                stones.append(y)
        if stones==[]:
            return 0
        else:
            return stones[0]
        