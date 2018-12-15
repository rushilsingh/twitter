import twitter
import time
import json


try:
    with open("credentials.json") as f:
        CREDENTIALS = json.load(f)
except Exception as e:
    print(e)
    print("Unable to import credentials")
    CREDENTIALS = {}


def manipulate(api, action):
    users = api.GetFollowers(screen_name=CREDENTIALS["screen_name"])
    users = [user.screen_name for user in users]
    if action=="unlike":
        destroy = api.DestroyFavorite
        tweets = api.GetFavorites(count=1000)
        tweet_ids = [str(tweet.id) for tweet in tweets if tweet.user.screen_name not in users]
    elif action == 'delete':
        destroy = api.DestroyStatus
        tweets = api.GetReplies(count=1000)
        retweets = api.GetUserRetweets(count=1000)
        tweets.extend(retweets)
        tweets = list(set(tweets))
        tweet_ids = [str(tweet.id) for tweet in tweets if tweet.favorite_count == 0 and tweet.in_reply_to_screen_name not in users]

    try:
        count = 0
        [destroy(status_id=tweet_id) for tweet_id in tweet_ids]
        count = len(tweet_ids)
    except Exception as e:
        print(e)
    time.sleep(0.5)

    print("Number of tweets %sd: %s\n" % (action, count))

def main():

    from sys import argv

    api = twitter.Api(consumer_key=CREDENTIALS["consumer_key"],
                      consumer_secret=CREDENTIALS["consumer_secret"],
                      access_token_key=CREDENTIALS["accesss_token_key"],
                      access_token_secret=CREDENTIALS["access_token_secret"]

    args = argv[1:]
    args = tuple(args)
    manipulate(api, *args)


if __name__ == "__main__":
    main()
