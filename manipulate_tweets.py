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


def get_tweet_ids(api, action, *args):

    users = api.GetFollowers(screen_name=CREDENTIALS["screen_name"])
    users = [user.screen_name for user in users]
    if action=="unlike":
        destroy_func = api.DestroyFavorite
        tweets = api.GetFavorites(count=1000)
        tweet_ids = [str(tweet.id) for tweet in tweets if tweet.user.screen_name not in users]
    elif action == 'delete':
        destroy_func = api.DestroyStatus
        tweets = api.GetReplies(count=1000)
        retweets = api.GetUserRetweets(count=1000)
        tweets.extend(retweets)
        tweets = list(set(tweets))
        tweet_ids = [str(tweet.id) for tweet in tweets if tweet.favorite_count == 0 and tweet.in_reply_to_screen_name not in users]

        return tweet_ids, destroy_func

def destroy(api, action, *args):

    tweet_ids, destroy_func  = get_tweet_ids(api, action, *args)
    try:
        count = 0
        [destroy_func(status_id=tweet_id) for tweet_id in tweet_ids]
        count = len(tweet_ids)
    except Exception as e:
        print(e)
    time.sleep(0.5)

    print("Number of tweets %sd: %s\n" % (action, count))

def main():

    from sys import argv
    if CREDENTIALS:
        try:
            api = twitter.Api(consumer_key=CREDENTIALS["consumer_key"],
                      consumer_secret=CREDENTIALS["consumer_secret"],
                      access_token_key=CREDENTIALS["accesss_token_key"],
                      access_token_secret=CREDENTIALS["access_token_secret"]
            args = argv[1:]
            args = tuple(args)
            manipulate(api, *args)
        except Exception as e:
            print(e)
    else:
        pass


if __name__ == "__main__":
    main()
