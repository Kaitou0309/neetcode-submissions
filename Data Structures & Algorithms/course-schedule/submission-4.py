class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        pre_req = {n: [] for n in range(numCourses)}

        for i, j in prerequisites: 

            pre_req[i].append(j)

        visited = set()
        completed = set()
        def dfs(node):
            
            if node in visited: 
                return False 

            if node in completed:
                return True

            visited.add(node)

            for nei in pre_req[node]:
                if not dfs(nei):
                    return False
            visited.remove(node)
            completed.add(node)

            return True

        for course in pre_req: 
            res = dfs(course)

            if not res:
                return False

        return True

