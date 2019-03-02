import json
import csv
import glob

def ordre(json):
    try:
        return int(json["id"])
    except KeyError:
        return 0



def mergeJson():
    data = {}
    result = []
    for f in glob.glob("resTache*.json"):
        with open(f, "r") as infile:
            tmp_json = json.load(infile)['tweets']
            #print(len(tmp_json))
            result.extend(tmp_json)

    data['tweets'] = result
    with open("jsonCompletv3.json", "w") as outfile:
        json.dump(data,outfile)


def sortJson():
    lignes = []
    with open('jsonCompletv3.json', encoding='utf8') as f:
        data = json.load(f)

    for i in data['tweets']:
        lignes.append(i)

    print(len(lignes))

    lignes.sort(key=ordre)
    data2 = {}
    data2['tweets'] = lignes
    with open("jsonCompletTriev3.json", "w") as outfile:
        json.dump(data2,outfile)


def main():

    #uncomment to merge the json files
    mergeJson()
    #return 0;
    
    #uncomment to sort the big json file
    jsonSorted = sortJson()
    #return 0

    #match Tweets with sorted files
    with open('jsonCompletTriev3.json', encoding='utf8') as f:
        leftFile = json.load(f)
    
    with open('iot-tweets-2009-2016.tsv',encoding='utf8') as tsvfile, open("iot-tweets-2009-2016-completv3.tsv", "w",encoding='utf8') as out_file:
        #lecture fichier original
        reader = csv.DictReader(tsvfile, dialect='excel-tab')


        #ecriture fichier sortie
        w = csv.writer(out_file, delimiter='\t')
        w.writerow(['TweetID', 'Sentiment', 'TopicID', 'Country', 'Gender', 'URLs','Text','User_ID', 'User_Name', 'Date', 'Hashtags', 'Indication'])

        #start searching
        indexLeftFile = 0
        totalLeftFile = len(leftFile['tweets'])
        print(totalLeftFile)
        counter = 0
        for row in reader:
            idr = row["TweetID"]
            idl = leftFile['tweets'][indexLeftFile]['id']

            while (idl < idr) and (indexLeftFile<totalLeftFile):
                indexLeftFile+=1
                idl = leftFile['tweets'][indexLeftFile]['id']

            if idr < idl:
                #not found
                line = [idr, row['Sentiment'], row['TopicID'], row['Country'], row['Gender'], row['URLs'],'','','','','','']
                w.writerow(line)
                continue

            if idl == idr:
                line = [idr, row['Sentiment'], row['TopicID'], row['Country'], row['Gender'], row['URLs'],leftFile['tweets'][indexLeftFile]['text'],leftFile['tweets'][indexLeftFile]['user_id'],leftFile['tweets'][indexLeftFile]['user_name'],leftFile['tweets'][indexLeftFile]['date'],leftFile['tweets'][indexLeftFile]['hashtags'],leftFile['tweets'][indexLeftFile]['indication']]
                w.writerow(line)
                counter+=1
                #print ('tweet trouvé')
                indexLeftFile +=1

        print(counter)
    return 0


if __name__ == "__main__":
    main()
