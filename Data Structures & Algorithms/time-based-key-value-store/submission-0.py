class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # [] here is a default that we give if key does not exist
        values = self.store.get(key, [])
        best_time = 0
        
        n = len(values)
        l, r = 0, n - 1

        while l <= r: 
            mid = (l + r) // 2

            if values[mid][1] <= timestamp: 

                best_time = values[mid][1] 
                res = values[mid][0]
                
                l = mid + 1
            
            else: 
                r = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)