import twitter
import time


def manipulate(api, action):
    users = api.GetFollowers(screen_name="")
    users = [user.screen_name for user in users]
    if action=="unlike":
        tweets = api.GetFavorites(count=1000)
        tweet_ids = [str(tweet.id) for tweet in tweets if tweet.screen_name not in users]
    elif action == 'delete':
        tweets = api.GetReplies(count=1000)
        tweet_ids = [str(tweet.id) for tweet in tweets if tweet.favorite_count == 0 and tweet.in_reply_to_screen_name not in users]

    try:
        print(action)
        if action == "unlike":
            api.DestroyFavorite(status_id=tweet_id)
        elif action == "delete":
            api.DestroyStatus(status_id=tweet_id)
        count += 1
    except Exception as e:
        print(e.message)
    time.sleep(0.5)

    print("Number of tweets %sd: %s\n" % (count, action))

def main():

    from sys import argv

    api = twitter.Api(consumer_key="",
                      consumer_secret="",
                      access_token_key="",
                      access_token_secret="")

    args = argv[1:] 
    args = tuple(args)
    manipulate(api, *args)


if __name__ == "__main__":
    main()
