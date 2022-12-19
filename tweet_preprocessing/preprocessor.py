import csv
import pandas as pd
import string
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer

def Tweet_Preprocess(tweetlist):
    #tweets mined which is comes as a list of strings tweetlist
    #limit is the number of tweets

    clean_txt=[]

    #convert to lower case
    clean_txt.append(tweetlist.str.lower())

    #remove punctuations
    def remove_punctuations(text):
        punctuations=string.punctuation
        return text.translate(str.maketrans('','',punctuations))

    #tf['clean_txt']=tf['clean_txt'].apply(lambda x:remove_punctuations(x))

    #remove stopwords
    STOPWORDS=set(stopwords.words('english'))
    def remove_stopwords(text):
        return ' '.join([word for word in text.spilt() if word not in STOPWORDS])
    
    txt=[]
    for x in clean_txt:
        txt.append(remove_stopwords(x))

    #can remove frequent words and rare words if needed
    #remove special characters and punctuations
    def remove_spl_chars(text):
        text=re.sub('[^a-zA-Z)-9]'," ",text)
        text=re.sub('\s+',' ',text)
        return text

    clean_txt=[]
    for x in txt:
        clean_txt.append(remove_spl_chars(x))

    #stemming
    ps=PorterStemmer()
    def stem_words(text):
        return " ".join([ps.stem(word) for word in text.split()])

    txt=[]
    for x in clean_txt:
        txt.append(stem_words(x))

    #remove URLs
    def remove_url(text):
        return re.sub(r'https?://\S+|www\.\S+', text)

    clean_txt=[]
    for x in txt:
        clean_txt.append(remove_url(x))

    #remove html tags
    def remove_html_tags(text):
        return re.sub(r'<.*?>','',text)

    txt=[]
    for x in clean_txt:
        txt.append(remove_html_tags(x))


    #can perform spelling correction
    # remove twitter handles
    def remove_pattern(input_txt,pattern):
        r=re.findall(pattern, input_txt)
        for word in r:
            input_txt=re.sub(word, "",input_txt)
        return input_txt

    clean_txt = [" ".join([word for word in tweet.split() if not word.startswith('@')]) for tweet in txt]

    #tweettxt=open("cleaned.txt")

    #can do tokenization
