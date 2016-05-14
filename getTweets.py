import twitter, json, sys, time
import codecs

consumer_key = "FBQBppfsDOSZqyTezocvvcmaH"
consumer_secret = "SpVeH49YPu2qOsYFgc9idet1X60vHizqMZ1jldMvvRxQ62mJNJ"
acc_token = "148870362-S4xnH0raocfrufnkJ66NufWeZwJJIDOTskSXMeTO"
acc_toke_secret = "HmXTkLmcrz4uZnVxkXAYLZhQhWZsJyj96Esm7AQo5iGeU"

auth = twitter.OAuth(acc_token, acc_toke_secret, consumer_key, consumer_secret)
twitter_api = twitter.Twitter(auth=auth)
q = "#dragonhack OR #dragonHack2016 OR @MLHacks"
count = 10000

max_id = sys.maxsize
retrieved = 0
out_file = "tweets.txt"
out_file = codecs.open(out_file, "a", "utf-8")
while retrieved < count:
    sr = twitter_api.search.tweets(q=q, count=count, max_id=max_id, result_type="mixed")
    retrieved = retrieved + int(len(sr["statuses"]))
    for tweet in sr["statuses"]:
        if not tweet["truncated"]:
            out_file.write(tweet["text"] + "\n")
        if max_id > int(tweet["id"]):
            max_id = int(tweet["id"])
    time.sleep(5)
print(retrieved)
# print(json.dumps(sr, indent=1))

#https://api.twitter.com/1.1/search/tweets.json?q