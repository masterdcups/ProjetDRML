import ijson
import csv
import tweepy
import pandas as pd

def to_csv(users,fav):
    with open('matrice_likes.csv', 'w', newline='',encoding='utf8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        #parcours de tout les pixels
        writer.writerow(["User_Name","Favorites_Tweets"])
        for i in range(len(users)):
            writer.writerow([users[i],fav[i]])


filename = 'iot-tweets-reduit-3.csv'
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


list_of_favorites = dict()
list_of_user = []

i = 0
u = 0
tot = 0

for user in users:
    try:

        #############################################
        #on regarde si on prend en compte le user à cause de la limite de l'API
        #print(user)
        test = api.lookup_users(user_ids=[user])
        a = test[0].favourites_count
        #print(a)

        if(a < 100):

            current_cursor = tweepy.Cursor(api.favorites, user_id=user,count=100)
            current_favorites = current_cursor.iterator.next()
            list_of_favorites[u] = []

            for favorite in current_favorites:
                #print(favorite.id)
                list_of_favorites[u].append(favorite.id)

            """

            next_cursor_id = current_cursor.iterator.next_cursor

            while next_cursor_id != 0:
                current_cursor = tweepy.Cursor(api.favorites, user_id=user, count=200, cursor=next_cursor_id)
                current_favorites = current_cursor.iterator.next()

                for favorite in current_favorites:
                    print(favorite.id)
                    list_of_favorites[u].append(favorite.id)


                next_cursor_id = current_cursor.iterator.next_cursor

            """

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


to_csv(list_of_user,list_of_favorites)

