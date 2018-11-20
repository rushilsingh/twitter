import twitter

protected_likes = []
protected_tweets = []
protected_replies = []

def manipulate(api, action):
    if action=="unlike":
        tweets = api.GetFavorites()
    tweet_ids = [tweet.id for tweet in tweets]
    try:
            if action =="unlike":
                    protected = protected_likes
            count = 0
            for tweet_id in tweet_ids:
                    if tweet_id in protected:
                        print "Protected tweet encountered"
                        continue
                    try:
                        if action == "unlike":
                            api.DestroyFavorite(status_id=tweet_id)
                    except Exception as e: print e
                    count += 1
                    time.sleep(0.5)
    except:
            pass

    print "Number of tweets: %s\n" % count

def main():

    api = twitter.Api(consumer_key="",
                      consumer_secret="",
                      access_token_key="",
                      access_token_secret="")

    manipulate(api, "unlike")


if __name__ == "__main__":
    main()
