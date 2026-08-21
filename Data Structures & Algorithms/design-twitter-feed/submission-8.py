from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.user_tweets = defaultdict(list)
        self.user_follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time, tweetId))
        self.user_follows[userId].add(userId)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(f"{self.user_follows=} | {self.user_tweets=}")
        feed = []
        heapq.heapify(feed)

        for tweeter_id in self.user_follows[userId]:
            tweets = self.user_tweets[tweeter_id]
            for tweet in tweets[-10:]:
                heapq.heappush(feed, tweet)
                # print(f"{feed=}")
        return [tweet[1] for tweet in heapq.nlargest(10, feed)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].discard(followeeId)
