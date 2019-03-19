import json
import ijson
import csv
import sys, csv, operator

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

    fileout = open('corpusLightComplet.csv', "a", encoding='utf-8')
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

    with open("CorpusLightComplet.csv", "r", encoding='utf-8') as infile:
        reader = csv.reader(infile,delimiter='\t')
        sortedlist = sorted(reader, key=operator.itemgetter(1))
        # now write the sorte result into new CSV file
        with open("CorpusLightCompletTrie.csv", "wb", encoding='utf-8') as f:
            fileWriter = csv.writer(f, delimiter='\t')
            for row in sortedlist:
                fileWriter.writerow(row)






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

sort()



