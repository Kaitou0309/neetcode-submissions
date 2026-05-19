class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        speed = 0

        i = 1  # eat at least 1 banana
        j = max(piles)

        min_k = j

        while i <= j:

            k = (i + j) // 2  # eat speed

            time = 0

            for val in piles:

                time = time + math.ceil(val / k)

            if time > h:
                i = k + 1
            else:
                min_k = min(min_k, k)
                j = k - 1

        return min_k


"""
piles = [3,6,7,11], h = 8

i = 1
j = 11

m = (1 + 11) // 2 = 6
[3,6,7,11]
hour 1 -> 3
hour 2 -> 6
hour 3 -> 6
hour 4 -> 1
hour 5 -> 6
hour 6 -> 5

banana eating speed = 6 -> 6 hours < 8 = h

m = (7 + 11) // 2 = 9
"""
