class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        dist_list = []
        
        for x, y in points:

            dist = math.sqrt((x ** 2) + (y ** 2))

            dist_list.append([dist, x, y])

        heapq.heapify(dist_list)

        res = []
        i = 0
        while i < k:
            dist, x, y = heapq.heappop(dist_list)
            res.append([x,y])
            i += 1

        return res

            

        


        

        