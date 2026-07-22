import heapq
from collections import deque

class Twitter:

    def __init__(self):
        self.user_followers = {}
        self.tweet_heap = [] # (time posted, [user_id, tweet_id])
        self.tweet_queue = deque([]) # (time posted, [user_id, tweet_id])
        self.timer = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        print(self.tweet_heap)
        heapq.heappush(self.tweet_heap, (self.timer, [userId, tweetId]))
        self.timer -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        while self.tweet_heap and len(feed) < 10:
            recent_tweet = heapq.heappop(self.tweet_heap)
            if recent_tweet[1][0] == userId or (userId in self.user_followers and recent_tweet[1][0] in self.user_followers[userId]):
                feed.append(recent_tweet[1][1])
            self.tweet_queue.append(recent_tweet)
        
        while self.tweet_queue:
            heapq.heappush(self.tweet_heap, self.tweet_queue.pop())

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_followers:
            self.user_followers[followerId].add(followeeId)
        else:
            self.user_followers[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_followers:
            self.user_followers[followerId].discard(followeeId)
