class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        res = float("inf")

        piles.sort() 

        l, r = 1, max(piles)
        while l <= r: 
            m = (l + r) // 2

            count = 0

            for i in range(len(piles)):

                count += math.ceil(piles[i] / m)

            if count > h:
                l = m + 1
                # print(l)
            else:
                res = min(res, m)
                r = m - 1

        return res
            

