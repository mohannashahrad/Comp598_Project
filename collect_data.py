import tweepy as tw
import pandas as pd

consumer_key= 'r6lmTLbU4g2uFAxqSrwreE3xj'
consumer_secret= 'yCdol7xzbO7Yq5oeEhxDr4Qcddk8a4JfymkYjkUHL6u26ygYuy'
access_token= '1460049054340104196-orfM1kheNtZk6iPbf5mepfsNmykUaW'
access_token_secret= 'PdYhwhNofVSuY0cMTxZ6fXzoaVDE9dDItiuISSKkQTVQU'
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

words = ['Covid', 'vaccination', 'Pfizer', 'Moderna', 'corona', 'AstraZeneca', 'Janssen']
geocodes = ['56.988998,-133.811869,1500km', '55.705271,-77.549072,1500km']
df=pd.DataFrame()
for word in words:
    for geocode in geocodes:
        tweets = tw.Cursor(api.search_tweets, q=word, lang='en', geocode=geocode).items(1500)
        clean_tweets = [[tweet.id, tweet.text, tweet.created_at, tweet.user.location] for tweet in tweets]
        tweet_text = pd.DataFrame(data=clean_tweets, columns=['id','text','time', 'location'])
        if (words.index(word) == 0) and (geocodes.index(geocode) == 0):
            tweet_text.to_csv('collected_data.csv', mode='w')
        else:
            tweet_text.to_csv('collected_data.csv', mode='a', header=False)
