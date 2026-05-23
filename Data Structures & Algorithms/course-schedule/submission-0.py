class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq_map = {i : [] for i in range(numCourses)}

        for a, b in prerequisites: 
            prereq_map[a].append(b)

        visited = set() 

        def dfs(course): 
            # false if cycle detected 
            if course in visited: 
                return False 

            # true if no prereq found
            if prereq_map[course] == []: 
                return True

            visited.add(course)

            for pre in prereq_map[course]: 
                if dfs(pre) is False: 
                    return False

            visited.remove(course)

            prereq_map[course] = []

            return True 

        
        for course in range(numCourses): 
            if dfs(course) is False: 
                return False 

        return True