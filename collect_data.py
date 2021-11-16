import tweepy as tw
import pandas as pd

consumer_key= 'r6lmTLbU4g2uFAxqSrwreE3xj'
consumer_secret= 'yCdol7xzbO7Yq5oeEhxDr4Qcddk8a4JfymkYjkUHL6u26ygYuy'
access_token= '1460049054340104196-orfM1kheNtZk6iPbf5mepfsNmykUaW'
access_token_secret= 'PdYhwhNofVSuY0cMTxZ6fXzoaVDE9dDItiuISSKkQTVQU'
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

hashtags = ['Covid', 'vaccination', 'Pfizer', 'Moderna']
df=pd.DataFrame()
for hashtag in hashtags:
    tweets = tw.Cursor(api.search_tweets, q=hashtag, lang="en", result_type="recent").items(1000)
    clean_tweets = [[tweet.id, tweet.text, tweet.created_at, tweet.user.location] for tweet in tweets]
    tweet_text = pd.DataFrame(data=clean_tweets, columns=['id','text','time', 'location'])
    if hashtags.index(hashtag) == 0:
        tweet_text.to_csv('data2.csv', mode='w')
    else:
        tweet_text.to_csv('data2.csv', mode='a', header=False)
