import csv

def geoTopic(outfile):
    fileout = open(outfile, "w", encoding='utf-8',newline='')
    writer = csv.writer(fileout, delimiter=',')

    with open('iot-tweets-2009-2016-topic.tsv', "r", encoding='utf-8') as infile:
        csv_reader = csv.reader(infile, delimiter='\t')
        column = next(csv_reader)

        for row in csv_reader:
            if(row[20] == '5'):

                country = row[3]
                ligne = [country]
                writer.writerow(ligne)

def sort():
    with open('geoTopic5.csv', encoding='utf-8') as csv_data:
        reader = csv.reader(csv_data, delimiter=',')
        # sorting with ID
        id_sorted = sorted(reader, key=lambda x: x[0], reverse=False)

        with open("geoTopic5-Trie.csv", "w",encoding='utf-8',newline='') as f:

            fileWriter = csv.writer(f, delimiter='\t')

            for row in id_sorted:
                ligne = [row[0]]
                fileWriter.writerow(ligne)

def countByCountry(infile,outfile):
    fileout = open(outfile, "w", encoding='utf-8', newline='')
    writer = csv.writer(fileout, delimiter=',')

    with open(infile, "r", encoding='utf-8') as infile:
        csv_reader = csv.reader(infile, delimiter='\t')
        country2 = 'null'
        nbt = 1
        for row in csv_reader:
            country1 = row[0]

            if (country1 == country2):
                nbt = nbt + 1
            else:
                ligne = ["['"+country2+"'",str(nbt)+"]"]
                writer.writerow(ligne)
                nbt = 1

            country2 = country1

def tradCountry(infile,outfile):
    fileout = open(outfile, "w", encoding='utf-8', newline='')
    writer = csv.writer(fileout, delimiter=',')

    with open(infile, "r", encoding='utf-8') as infile:
        csv_reader = csv.reader(infile, delimiter='\t')
        for row in csv_reader:
            country = row[0]
            with open('country.csv', "r", encoding='utf-8') as infile:
                csv_reader = csv.reader(infile, delimiter=';')
                for row2 in csv_reader:
                    country2 = row2[0]
                    if (country == country2):
                        ligne = ["['"+row2[3]+"'", row[1]+"]"]
                        writer.writerow(ligne)









geoTopic('geoTopic5.csv')
sort()
countByCountry('geoTopic5-Trie.csv', 'geoTopic5Count.csv')