import json
import ijson
import csv
import sys, csv, operator
#from csvsort import csvsort



def fullToLigth(filein,fileout):

    #alltweets = {'tweets': []}

    with open(filein, "r",encoding='utf-8') as infile:

        fileout = open(fileout, "w", encoding='utf-8',newline='')
        writer = csv.writer(fileout, delimiter='\t')

        columns = [
            'created_at',
            'id_str',
            'text',
            'source',
            'in_reply_to_status_id_str',
            'in_reply_to_user_id_str',
            'user.id_str',
            'user.name',
            'user.location',
            'user.followers_count',
            'coordinates',
            'quoted_status_id_str',
            'is_quote_status',
            'hashtags',
            'retweeted',
            'urls'
        ]

        writer.writerow(columns)

        tweets = ijson.items(infile, 'tweets.item')
        #t = {}
        for tweet in tweets:
            row = [tweet.get('created_at', ""),
                   tweet.get('id_str', ""),
                   tweet.get('text', ""),
                   tweet.get('source', ""),
                   tweet.get('in_reply_to_status_id_str', ""),
                   tweet.get('in_reply_to_user_id_str', ""),
                   tweet['user'].get('id_str', ""),
                   tweet['user'].get('name', ""),
                   tweet['user'].get('location', ""),
                   tweet['user'].get('followers_count', ""),
                   tweet.get('coordinates', ""),
                   tweet.get('quoted_status_id_str', ""),
                   tweet.get('is_quote_status', ""),
                   tweet.get('retweeted', ""),
                   tweet['entities'].get('hashtags', ""),
                   tweet['entities'].get('urls', "")
                   ]
            writer.writerow(row)

            #alltweets['tweets'].append(t)

def merge(filein):

    fileout = open('iot-tweets-2009-2016-corrige2.tsv', "a", encoding='utf-8')
    writer = csv.writer(fileout, delimiter='\t')

    with open(filein, "r", encoding='utf-8') as infile:
        csv_reader = csv.reader(infile, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                ligne = [row[0],
                       row[1],
                       row[2],
                       row[3],
                       row[4],
                       row[5],
                       row[6],
                       row[7],
                       row[8],
                       row[9],
                       row[10],
                       row[11],
                       row[12],
                       row[13],
                       row[14],
                       row[15],
                       ]
                writer.writerow(ligne)

                line_count += 1

def sort():
    with open('lda_conv1_6t.csv', encoding='utf-8') as csv_data:
        reader = csv.reader(csv_data, delimiter=',')
        # sorting with ID
        header = next(reader)
        id_sorted = sorted(reader, key=lambda x: int(x[0]), reverse=False)

        with open("ida_conv1_6t-Trie.tsv", "w",encoding='utf-8',newline='') as f:

            fileWriter = csv.writer(f, delimiter='\t')
            columns = [
                'TweetID',
                'TopicID'
            ]

            fileWriter.writerow(columns)
            for row in id_sorted:
                ligne = [row[0],
                        row[1]
                        ]
                fileWriter.writerow(ligne)

def join():

    with open('corpusLightTrie0.csv', encoding='utf8') as f:
        # lecture fichier original
        leftFile = csv.reader(f,dialect='excel-tab')
        #leftFile = csv.DictReader(f, dialect='excel-tab')


        with open('iot-tweets-2009-2016-Trie.tsv', encoding='utf8') as tsvfile, open("iot-tweets-2009-2016-0.tsv", "w",
                                                                                encoding='utf8',newline='') as out_file:

            reader = csv.DictReader(tsvfile, dialect='excel-tab')

            # ecriture fichier sortie
            w = csv.writer(out_file, delimiter='\t')
            w.writerow(
                ['TweetID', 'Sentiment', 'TopicID', 'Country', 'Gender', 'URLs',
                 'Created_at', 'Text', 'Source', 'in_reply_to_status_id_str',
                 'in_reply_to_user_id_str', 'User_id', 'User_name'
                 , 'User_location', 'User_followers_count', 'Coordinates', 'quoted_status_id_str'
                 , 'is_quote_status', 'Entities_hashtags', 'Entities_urls'])



            # start searching
            data = list(leftFile)
            totalLeftFile = len(data)
            f.seek(0)


            print(totalLeftFile)
            counter = 0

            passer = True

            for row in reader:
                idr = row["TweetID"]

                if(passer):
                    leftRow = next(leftFile)
                    idl = leftRow[1]
                #print(idl, "   ", idr)

                if(idl == 'id_str'):
                    break
                #idl = leftFile['tweets'][indexLeftFile]['id']
                #print(indexLeftFile, "< ?", totalLeftFile-2)

                while (int(idl) < int(idr)):
                    #idl = leftFile['tweets'][indexLeftFile]['id']
                    leftRow = next(leftFile)
                    idl = leftRow[1]


                if int(idr) < int(idl):
                    # not found
                    """
                    line = [idr, row['Sentiment'], row['TopicID'], row['Country'], row['Gender'], row['URLs'], '', '', '',
                            '', '', '', '', '', '', '', '', '', '', '']
                    w.writerow(line)
                    """
                    #print(idr)

                    passer = False
                    continue

                if int(idl) == int(idr):
                    line = [idr, row['Sentiment'], row['TopicID'], row['Country'], row['Gender'], row['URLs'],
                            leftRow[0],leftRow[2],leftRow[3],leftRow[4],leftRow[5],leftRow[6],leftRow[7],leftRow[8],leftRow[9],
                            leftRow[10],leftRow[11],leftRow[12],leftRow[13]]
                    w.writerow(line)
                    counter += 1
                    # print ('tweet trouvé')
                    passer = True

    

            print(counter)


    pass


def addTopic():
    with open('ida_conv1_6t-Trie.tsv', encoding='utf8') as f:
        # lecture fichier original
        leftFile = csv.reader(f, dialect='excel-tab')
        # leftFile = csv.DictReader(f, dialect='excel-tab')

        with open('iot-tweets-2009-2016-corrige2.tsv', encoding='utf8') as tsvfile, open("iot-tweets-2009-2016-topic.tsv", "w",
                                                                                     encoding='utf8',
                                                                                     newline='') as out_file:

            reader = csv.DictReader(tsvfile, dialect='excel-tab')

            # ecriture fichier sortie
            w = csv.writer(out_file, delimiter='\t')
            w.writerow(
                ['TweetID', 'Sentiment', 'TopicID', 'Country', 'Gender', 'URLs',
                 'Created_at', 'Text', 'Source', 'in_reply_to_status_id_str',
                 'in_reply_to_user_id_str', 'User_id', 'User_name'
                    , 'User_location', 'User_followers_count', 'Coordinates', 'quoted_status_id_str'
                    , 'is_quote_status', 'Entities_hashtags', 'Entities_urls','LDA_Topic'])

            # start searching
            data = list(leftFile)
            totalLeftFile = len(data)
            f.seek(0)

            print(totalLeftFile)
            counter = 0

            #skip header
            leftRow = next(leftFile)


            passer = True


            for row in reader:
                idr = row["TweetID"]

                if (passer):
                    leftRow = next(leftFile)
                    idl = leftRow[0]

                while (int(idl) < int(idr)):
                    # idl = leftFile['tweets'][indexLeftFile]['id']
                    leftRow = next(leftFile)
                    idl = leftRow[1]

                if int(idr) < int(idl):
                    # not classified
                    line = [idr,row['Sentiment'],row['TopicID'],row['Country'],row['Gender'],row['URLs'],
                            row['Created_at'],row['Text'],row['Source'],row['in_reply_to_status_id_str'],
                            row['in_reply_to_user_id_str'],row['User_id'],row['User_name'],row['User_location'],
                            row['User_followers_count'],row['Coordinates'],row['quoted_status_id_str'],row['is_quote_status'],
                            row['Entities_hashtags'],row['Entities_urls'],'-1']

                    w.writerow(line)

                    # print(idr)

                    passer = False
                    continue

                if int(idl) == int(idr):
                    line = [idr,row['Sentiment'],row['TopicID'],row['Country'],row['Gender'],row['URLs'],
                            row['Created_at'],row['Text'],row['Source'],row['in_reply_to_status_id_str'],
                            row['in_reply_to_user_id_str'],row['User_id'],row['User_name'],row['User_location'],
                            row['User_followers_count'],row['Coordinates'],row['quoted_status_id_str'],row['is_quote_status'],
                            row['Entities_hashtags'],row['Entities_urls'],leftRow[1]]
                    w.writerow(line)
                    counter += 1
                    # print ('tweet trouvé')
                    passer = True

            print(counter)

    pass



"""
fullToLigth("corpus0.json",'corpusLight0.csv')
fullToLigth("corpus1.json",'corpusLight1.csv')
fullToLigth("corpus2.json",'corpusLight2.csv')
fullToLigth("corpus3.json",'corpusLight3.csv')
fullToLigth("corpus4.json",'corpusLight4.csv')

merge("corpusLight1.csv")
merge("corpusLight2.csv")
merge("corpusLight3.csv")
merge("corpusLight4.csv")
"""

#sort()


#join()

"""
merge("iot-tweets-2009-2016-1.tsv")
merge("iot-tweets-2009-2016-2.tsv")
merge("iot-tweets-2009-2016-3.tsv")
merge("iot-tweets-2009-2016-4.tsv")
"""


#sort()

addTopic()

