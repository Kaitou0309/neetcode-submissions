class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        


        graph = defaultdict(list)
        indegree = [0] * numCourses
        res = []

        for course, pre in prerequisites: 
            graph[pre].append(course)
            indegree[course] += 1

        q = deque() 

        for course in range(numCourses): 
            if indegree[course] == 0: 
                q.append(course)
                res.append(course)


        

        while q: 
            course = q.popleft() 

            for next_course in graph[course]: 
                indegree[next_course] -= 1
                if indegree[next_course] == 0: 
                    q.append(next_course)
                    res.append(next_course)

        if len(res) == numCourses: 
            return res 
        
        return []
        

