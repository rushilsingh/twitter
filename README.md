# Twitter Automation Tools

To run:
```
make prepare-venv
python manipulate_tweets.py delete
python manipulate_tweets.py unlike
```


The current python script is used for the following purposes:
1. To delete all tweets that have not been liked and are not in response to one of your followers.
2. To unlike all tweets that are not tweeted by one of your followers

Note:
You have to insert your screen name, and various api keys in the file credentials.json. The current values are just examples.
