class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position,speed))
        cars.sort(reverse=True)
        fleet=0
        last_time=0
        for p,s in cars:
            time=(target-p)/s
            if time > last_time:
                last_time=time
                fleet+=1

        return fleet
            
       