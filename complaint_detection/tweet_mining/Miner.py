#import json
#import langdetect
import tweepy as tp
import configparser
#import GetOldTweets3 as got

def TweetMiner(limit):
	#Setting up key config file parser
	config=configparser.RawConfigParser()
	config.read(r"complaint_detection/tweet_mining/apiconfig.ini")

	#Setting up API keys
	api_key=config['Twitter']['API_KEY']
	api_key_secret=config['Twitter']['API_KEY_SECRET']
	bearer_token=config['Twitter']['BEARER_TOKEN']
	access_token=config['Twitter']['ACCESS_TOKEN']
	access_token_secret=config['Twitter']['ACCESS_TOKEN_SECRET']

	auth = tp.OAuthHandler(api_key, api_key_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tp.API(auth)

	#Setting up output files
	#file=open("tweets.txt",'w')

	#Setting up authentication
	#auth=tp.OAuthHandler(api_key,api_key_secret)
	#auth.set_access_token(access_token,access_token_secret)
	client=tp.Client(bearer_token=bearer_token)

	#Initializing API Object
	#api=tp.API(auth)

	#Loading search query parameters
	#query_file=json.load(open('query.json','r'))

	#Setting up search queries
	user='PoliceSight'
	#id=api.get_user(username=user).data.id

	#Extracting Tweets
	#tweets=api.user_timeline(screen_name=username,count=limit,tweet_mode='extended')
	#tweets=api.get_users_mentions(id,max_results=limit)
	tweets=client.search_recent_tweets(query="Police",tweet_fields=['context_annotations','created_at'],max_results=10)
	tweetlist=[]
	#print(tweets)
	for i,tweet in enumerate(tweets.data):
		#if langdetect.detect(str(tweet))=='en':

		#Remove duplicate tweets
		if tweet not in tweetlist:
			tweetlist.append(tweet.text)
	#print(tweet.text)

	#print(tweetlist)

	'''
	hashtag='#keralapolice'
	query_stmt=hashtag+' lang:en '+'-filter:retweets'
	client.user
	tweets=client.search_recent_tweets(query=query_stmt,tweet_fields=['context_annotations','created_at'],max_results=100)

	print(str(tweets))
	file.write(str(tweets))

	tweetlist=[]

	for i,tweet in enumerate(tweets.data):
	tweetlist.append({i+1:tweet.text})
	print(tweet.context_annotations)

	'''
	return tweetlist
