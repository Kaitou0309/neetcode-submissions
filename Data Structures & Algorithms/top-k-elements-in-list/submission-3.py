class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        hash_map = {}

        for n in nums: 
            hash_map[n] = hash_map.get(n, 0) + 1

        
        
        i = 0 
        res = []
        while i < k: 
            curr = max(hash_map.values())
            for key in hash_map.keys():

                if hash_map[key] == curr: 
                    res.append(key)
                    del hash_map[key]
                    i += 1
                    break

        return res
            

        
        


        

