class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1: 
            return False


        graph = defaultdict(list)

        for parent, child in edges: 
            graph[parent].append(child)
            graph[child].append(parent)

        visited = set() 

        def dfs(node): 
            if node in visited: 
                return

            visited.add(node)

            for child in graph[node]: 
                dfs(child)

        dfs(0)

        return len(visited) == n