class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        dist_list = []

        for i in range(len(points)):

            x = points[i][0]
            y = points[i][1]
            coord = [x, y]

            dist = math.sqrt(x**2 + y**2)

            dist_list.append((dist, coord))

        heapq.heapify(dist_list)

        res = []

        for i in range(k): 

            val, coord = heapq.heappop(dist_list)

            res.append(coord)

        return res


        
        