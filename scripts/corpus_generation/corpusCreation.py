#!/usr/bin/env python
# coding: utf-8

# In[63]:

import json
import ijson

def fullToLigth():

    alltweets = {'tweets': []}
    with open("corpus0.json", "r") as infile:

        tweets = ijson.items(infile, 'tweets.item')
        t = {}
        for tweet in tweets:
            t['created_at'] = tweet.get('created_at')
            t['id_str'] = tweet.get('id_str'),
            t['text'] = tweet.get('text'),
            t['source'] = tweet.get('source'),
            t['in_reply_to_status_id_str'] = tweet.get('in_reply_to_status_id_str'),
            t['in_reply_to_user_id_str'] = tweet.get('in_reply_to_user_id_str'),
            t['User_id_str'] = tweet['user'].get('id_str'),
            t['User_name'] = tweet['user'].get('name'),
            t['User_location'] = tweet['user'].get('location'),
            t['User_followers_count'] = tweet['user'].get('followers_count'),
            t['coordinates'] = tweet.get('coordinates'),
            t['quoted_status_id_str'] = tweet.get('quoted_status_id_str'),
            t['is_quote_status'] = tweet.get('is_quote_status'),
            t['retweeted'] = tweet.get('retweeted'),
            t['hashtags'] = tweet['entities'].get('hashtags'),

            alltweets['tweets'].append(t)



    # json_data = json.dumps(tweets)
    with open('corpusLight0.json', 'w') as outfile:
        json.dump(alltweets, outfile)



