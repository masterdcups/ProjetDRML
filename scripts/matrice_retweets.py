import ijson
import csv
import tweepy
import pandas as pd

def to_csv(users,ret):
    with open('matrice_retweets.tsv', 'w', newline='',encoding='utf8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["User_Name\tTweets_retweeted"])
        for i in range(len(users)):
            str_fav = "\t"
            for j in range(len(ret[i])):
                str_fav = str_fav + str(ret[i][j]) + "\t"
            writer.writerow([users[i]+str_fav])


filename = './sources/5000_users.csv'
data = pd.read_csv(filename,sep='\t', na_values=['null','None','',], dtype=object)
users = data['User_ID']


# Variables that contains the user credentials to access Twitter API compte de paul
ACCESS_TOKEN = '760574079170646016-0oviS7a5Smr5HBb1paanDjpPasTuvTm'
ACCESS_SECRET = 'iNGuwEM4ajIGGlfxWpVED1qPQISPSfvkOKpIk2qDpjFY5'
CONSUMER_KEY = 'IeFMYLNxlrF9yEhB6sNHjtn4g'
CONSUMER_SECRET = 'Tc1WTKEXGI3OSo5BRkRr4A2yUpVqotSuU2uGLpV4cUXOZgEkKE'

# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------


list_of_retweeted = dict()
list_of_user = []

i = 0
u = 0
tot = 0

for user in users:
    try:

        #############################################
        #on prend tout les users mais limite à 100 tweets total
        test = api.lookup_users(user_ids=[user])
        #print(test)


        current_cursor = tweepy.Cursor(api.user_timeline, user_id=user,count=100,include_rts = False)
        current_ret = current_cursor.iterator.next()
        list_of_retweeted[u] = []


        for retweets in current_ret:
            #print(retweets)

            #on ajoute seulement si le tweet à été retweet au moins une fois
            nbr = (retweets.retweet_count)
            if(nbr > 0):
                list_of_retweeted[u].append(retweets.id)


        list_of_user.append(test[0].screen_name)

        u += 1

    except (StopIteration):
        print("StopIteration")
        continue
    except :
        print("Other Exception")
        continue

    tot += 1

    print(u,"/",tot)


to_csv(list_of_user,list_of_retweeted)

