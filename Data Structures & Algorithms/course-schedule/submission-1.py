class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        prereq_map = {i : [] for i in range(numCourses)}

        for a, b in prerequisites:
            prereq_map[b].append(a)

        visited = set()

        def dfs(course): 

            if course in visited: 
                return False 

            if prereq_map[course] == []:
                return True

            visited.add(course)

            for prereq in prereq_map[course]:

                if dfs(prereq) is False:
                    return False 

            visited.remove(course)
            prereq_map[course] = []

            return True


        for i in range(numCourses):

            if dfs(i) is False:
                return False 

        return True
            

