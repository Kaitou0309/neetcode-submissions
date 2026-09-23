class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        # print(freq)

        for n in nums: 
            count[n] = count.get(n, 0) + 1

        for n, cnt in count.items():
            freq[cnt].append(n)
        # print(freq)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k: 
                    return res

        

