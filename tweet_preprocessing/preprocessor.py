import csv
import pandas as pd
import string
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer

def Tweet_Preprocess(tweetlist):

    #Setting up CSV file
    csvfile=csv.writer(open('tweet_preprocessing/tweets.csv','w'))
    fields=['Raw Tweets','Preprocessed Tweets']
    csvfile.writerow(fields)
    
    #Defining a new list for storing cleaned tweets
    clean_tweets=[]

    #   - Conversion to lowercase
    #   - Deletion of duplicate tweets
    for tweet in tweetlist:
        if tweet not in clean_tweets:
            clean_tweets.append(tweet.lower())
    
    #Remove punctuation marks
    for idx in range(len(clean_tweets)):
        clean_tweets[idx]=clean_tweets[idx].translate(str.maketrans('','',string.punctuation))
    
    #Remove stopwords
    stopwords_list=set(stopwords.words('english'))
    for idx in range(len(clean_tweets)):
        clean_tweets[idx]=' '.join([word for word in clean_tweets[idx].split() if word not in stopwords_list])

    #Removing frequent/rare words
    for idx in range(len(clean_tweets)):
        clean_tweets[idx]=re.sub('[^a-zA-Z)-9]'," ",clean_tweets[idx])
        clean_tweets[idx]=re.sub('\s+',' ',clean_tweets[idx])

    #Stemming
    ps=PorterStemmer()
    for idx in range(len(clean_tweets)):
        clean_tweets[idx]=" ".join([ps.stem(word) for word in clean_tweets[idx].split()])

    #Remove URLs
    for idx in range(len(clean_tweets)):
        clean_tweets[idx]=re.sub(r'https?://\S+|www\.\S+','',clean_tweets[idx])

    #Removing HTML Tags
    for idx in range(len(clean_tweets)):
        clean_tweets[idx]=re.sub(r'<.*?>','',clean_tweets[idx])

    #Removing Twitter Handles
    clean_tweets=[" ".join([word for word in tweet.split() if not word.startswith('@')]) for tweet in clean_tweets]

    #Writing raw and cleaned tweets to csv file
    rows=[]

    for idx in range(len(tweetlist)):
        rows.append([tweetlist[idx],clean_tweets[idx]])
    
    csvfile.writerows(rows)
