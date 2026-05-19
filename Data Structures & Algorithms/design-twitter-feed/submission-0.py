class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:

            tweets = self.tweetMap[followeeId]

            if tweets: 
                index = len(tweets) - 1
                count, tweetId = tweets[index]
                heapq.heappush(heap, [count, tweetId, followeeId, index - 1])

        while heap and len(res) < 10: 
            count, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0: 
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap, [count, tweetId, followeeId, index - 1])

        return res
                


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId: 
            self.followMap[followerId].discard(followeeId)
        
        
        
