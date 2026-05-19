class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        # use hashmap, key = number, value = count number
        for i in nums:

            if i in count_dict:
                count_dict[i] += 1
            else: 
                count_dict[i] = 1

        top_k = heapq.nlargest(k, count_dict.keys(), key=count_dict.get)
        print(top_k)
        return top_k