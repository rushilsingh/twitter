import twitter
import time

protected_likes = ["1063738463776894976"]
protected_tweets = []
protected = []

def manipulate(api, action, option):
    if action=="unlike":
        tweets = api.GetFavorites()
    elif action == 'delete':
        tweets = api.GetReplies()
        tweet_ids = [str(tweet.id) for tweet in tweets if tweet.favorite_count == 0]

    try:
            if action =="unlike":
                    protected = protected_likes
            elif action == "delete":
                    protected = protected_tweets
            count = 0
            for tweet_id in tweet_ids:
                if tweet_id in protected:
                        print("Protected tweet encountered")
                        continue
                try:
                    print(action)
                    if action == "unlike":
                        api.DestroyFavorite(status_id=tweet_id)
                    elif action == "delete":
                        api.DestroyStatus(status_id=tweet_id)
                except Exception as e:
                    print(e.message)
                count += 1
                time.sleep(0.5)
    except:
        pass

    print("Number of tweets: %s\n" % count)

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
