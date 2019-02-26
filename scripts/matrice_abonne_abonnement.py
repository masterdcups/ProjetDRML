import csv
import tweepy
import pandas as pd

def to_csv(users,followers,friends):

    with open('matrice_follower-following.csv', 'w', newline='',encoding='utf8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        #parcours de tout les pixels
        writer.writerow(["User_Name\tFollowers\tFriends"])
        for i in range(len(users)):
            writer.writerow([users[i]+"\t"+followers[i]+"\t"+friends[i]])



filename = './sources/10_users.csv'


data = pd.read_csv(filename,sep='\t', na_values=['null','None','',], dtype=object)

users = data['User_ID']



# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '736977163614867460-Ls5ETI5T4iyHnkLk5CrM9E6OocAEAfc'
ACCESS_SECRET = 'oRVZQmBufEwmoxN0TOM6RgDlRTpTCkaYkZ4krPlNtH5RU'
CONSUMER_KEY = 'uChtVb3tLBC9BryivVqXXS3xp'
CONSUMER_SECRET = 'a9toRioywMtuWwPEI6SKZ0SKB8xg6GwlScsC0Smpd10pn1WniE'

# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------


# Get the full list of followers of a particular user
list_of_followers = dict()

list_of_friends = dict()

list_of_user = []
i = 0
u = 0
tot = 0


for user in users:

    try:

        #############################################
        #on prend tout les users mais on se limite à 100 abonnés et 100 abonnements max
        test = api.lookup_users(user_ids=[user])
        a = test[0].followers_count
        b = test[0].friends_count



        #followers
        current_cursor = tweepy.Cursor(api.followers, user_id=user, count=100)
        current_followers = current_cursor.iterator.next()
        list_of_followers[u] = []

        #print("for user ",u,"nb follwers = ", len(current_followers))

        for follower in current_followers:
            name = follower.screen_name
            list_of_followers[u].append(name)

        if (a>100):
            list_of_followers[u].append("...etc")


        # following
        current_cursor2 = tweepy.Cursor(api.friends, user_id=user, count=100)
        current_friends = current_cursor2.iterator.next()

        list_of_friends[u] = []

        for friends in current_friends:
            name = friends.screen_name
            list_of_friends[u].append(name)


        if (b > 100):
            list_of_friends[u].append("...etc")

        u += 1

    except :
        print("Exception")
        continue


    tot += 1

    print(u,"/",tot)



#print(list_of_followers[0])

#print(list_of_friends[0])

to_csv(list_of_user,list_of_followers,list_of_friends)

