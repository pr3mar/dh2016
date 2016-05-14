import twitter
import json

consumer_key = "FBQBppfsDOSZqyTezocvvcmaH"
consumer_secret = "SpVeH49YPu2qOsYFgc9idet1X60vHizqMZ1jldMvvRxQ62mJNJ"
acc_token = "148870362-S4xnH0raocfrufnkJ66NufWeZwJJIDOTskSXMeTO"
acc_toke_secret = "HmXTkLmcrz4uZnVxkXAYLZhQhWZsJyj96Esm7AQo5iGeU"

auth = twitter.OAuth(acc_token, acc_toke_secret, consumer_key, consumer_secret)
twitter_api = twitter.Twitter(auth=auth)
q = "@MLHacks"
count = 1000
sr = twitter_api.search.tweets(q=q, count=count, until="2016-05-15", result_type="mixed")

print(len(sr["statuses"]))

for tweet in sr["statuses"]:
    print(tweet["text"])
# print(json.dumps(sr, indent=1))

#https://api.twitter.com/1.1/search/tweets.json?q