from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        # Global unique chronological timestamp sequence counter
        self.time = 0
        # Maps a userId to a list of their posted tweets: (timestamp, tweetId)
        self.tweets = defaultdict(list)
        # Maps a userId to a set of userIds they are following
        self.followees = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Use negative timestamps so the Python min-heap extracts higher values first
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        
        # Include the user's own timeline along with their followed feeds
        user_ids = set(self.followees[userId])
        user_ids.add(userId)
        
        # Seed the heap with the absolute newest single tweet from each distinct author
        for u_id in user_ids:
            if u_id in self.tweets:
                index = len(self.tweets[u_id]) - 1
                time, tweetId = self.tweets[u_id][index]
                # Store: negative timestamp, actual tweetId, author id, and preceding index pointer
                heapq.heappush(min_heap, (time, tweetId, u_id, index - 1))
                
        # Iteratively pull up to exactly 10 of the most chronological tweets
        while min_heap and len(res) < 10:
            time, tweetId, u_id, index = heapq.heappop(min_heap)
            res.append(tweetId)
            
            # If the specific user feed still has older items, push the next candidate
            if index >= 0:
                next_time, next_tweetId = self.tweets[u_id][index]
                heapq.heappush(min_heap, (next_time, next_tweetId, u_id, index - 1))
                
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)