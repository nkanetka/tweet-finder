from TwitterSearch import *

totalTweetCount = 0 # keeps track of the total number of tweets with the keyword

try:
	tso = TwitterSearchOrder()
	tso.add_keywords(['force awakens'])

	ts = TwitterSearch(
			consumer_key = '',
			consumer_secret = '',
			access_token = '',
			access_token_secret = ''
	)

	for tweet in ts.search_tweets_iterable(tso):
		totalTweetCount += 1
		print( 'Created at: %s, Text: %s ' % (  tweet['created_at'], tweet['text'] ) )

except TwitterSearchException as e:
	print(e)

print('there are a total of %s tweets!' % (totalTweetCount) )