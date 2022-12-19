from tweet_miner.miner import TweetMiner
from tweet_preprocessing import TweetPreprocess

if __name__=='__main__':
	limit=int(input("Numder of Tweets : "))
	tweetlist=TweetMiner(limit)
	TweetPreprocess(tweetlist)
