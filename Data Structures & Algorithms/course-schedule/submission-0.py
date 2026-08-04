from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=set()
        path=set()

        d={}
        for i,j in prerequisites:
            if j not in d:
                d[j]=[]
            d[j].append(i)

        def dfs(node,visited,d):
            visited.add(node)
            path.add(node)

            for nei in d.get(node, []):
                if nei in path:
                    return False

                if nei not in visited:
                    if dfs(nei,visited,d)==False:
                        return False

            path.remove(node)
            return True

        for node in d:
            if node not in visited:
                if dfs(node,visited,d)==False:
                    return False


        return True
               



        