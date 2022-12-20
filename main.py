from tweet_mining.miner import TweetMiner
from tweet_preprocessing.preprocessor import Tweet_Preprocess

if __name__=='__main__':
	limit=int(input("Numder of Tweets : "))
	tweetlist=TweetMiner(limit)
	Tweet_Preprocess(tweetlist)