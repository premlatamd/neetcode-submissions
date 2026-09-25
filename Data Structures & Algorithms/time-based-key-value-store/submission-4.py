class TimeMap:

    def __init__(self):
        self.d={}
    
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]={}
        self.d[key][timestamp]=value
        
      


        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        if timestamp in self.d[key]:
            return self.d[key][timestamp]
        else:
            mini=float("-inf")
            for i in self.d[key]:
                if i < timestamp:
                    mini=i
                    continue
                break
            if  mini==float("-inf"):
                return ""
            return self.d[key][mini]
