#!/usr/bin/env python
# coding: utf-8

# In[63]:


import json

# In[64]:


filename = 'inutile/resfinalbistrois4'

# In[65]:


tweets = {'tweets': []}
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        tweet = {}
        nbretweet = 0
        # convert to a valid json format
        #         line = line.replace("\"","\\\"")
        #         line = line.replace("'","\"")
        line = line.replace("True", "true")
        line = line.replace("False", "false")
        line = line.replace("None", "null")
        fields = line.split(',')

        for field in fields:
            text = field.strip()
            if text[0:4] == "'id'":
                tweet['id'] = text[5:].strip()
                break

        for field in fields:
            text = field.strip()
            if text[0:6] == "'text'":
                tweet['text'] = text[7:].strip()
                break
        for field in fields:
            text = field.strip()
            if text[0:13] == "'user': {'id'":
                tweet['user_id'] = text[14:].strip()
                break
        for field in fields:
            text = field.strip()
            if text[0:13] == "'screen_name'":
                tweet['user_name'] = text[14:].strip()
                break
        for field in fields:
            text = field.strip()
            if text[0:12] == "'created_at'":
                tweet['date'] = text[13:].strip()
                break

        search = False

        for field in fields:
            text = field.strip()

            if search:

                if text[0:9] != "'symbols'":
                    tweet['hashtags'] = tweet['hashtags'] + ', ' + text
                else:
                    search = False

            if text[0:23] == "'entities': {'hashtags'":
                tweet['hashtags'] = text[24:].strip()
                search = True

        is_reply = False
        is_retweet = False
        for field in fields:
            text = field.strip()
            if text[0:23] == "'in_reply_to_status_id'":
                if text[24:].strip() != 'null':
                    tweet['indication'] = 'reply'
                    is_reply = True
                    break

        if not (is_reply):
            for field in fields:
                text = field.strip()
                if text[0:18] == "'retweeted_status'":
                    is_retweet = True
            if (is_retweet):
                tweet['indication'] = 'retweet'
            else:
                tweet['indication'] = 'tweet'

        tweets['tweets'].append(tweet)

# In[66]:



# json_data = json.dumps(tweets)
with open('resTache4.json', 'w') as outfile:
    json.dump(tweets, outfile)


# In[67]:



# In[ ]:




