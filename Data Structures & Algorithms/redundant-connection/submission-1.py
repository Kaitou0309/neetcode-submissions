class DSU: 
    def __init__(self, n): 
        self.parents = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, n1): 
        res = n1
        while res != self.parents[res]: 
            self.parents[res] = self.parents[self.parents[res]]
            res = self.parents[res]

        return res 

    def union(self, n1, n2): 
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2: 
            return False

        if self.rank[p2] > self.rank[p1]: 
            self.parents[p1] = p2 
            self.rank[p2] += self.rank[p1]
        else: 
            self.parents[p2] = p1 
            self.rank[p1] += self.rank[p2]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        dsu = DSU(len(edges))

        for n1, n2 in edges: 
            if not dsu.union(n1, n2): 
                return [n1, n2]

        return


