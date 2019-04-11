import csv

def allDay():
    fileout = open('tweetPerDay.csv', "w", encoding='utf-8',newline='')
    writer = csv.writer(fileout, delimiter=',')

    with open('iot-tweets-2009-2016-topic.tsv', "r", encoding='utf-8') as infile:
        csv_reader = csv.reader(infile, delimiter='\t')
        column = next(csv_reader)
        nbt = 1
        day2 = 'null'
        for row in csv_reader:
            date = row[6].split(' ')
            day1 = date[1]+' '+date[2]+' '+date[5]
            if(day1 == day2):
                nbt = nbt + 1

            else:
                ligne = [day2, nbt]
                writer.writerow(ligne)
                nbt = 1


            day2 = day1
            #nbt = nbt + 1
            #print(day)

def allMonth():
    fileout = open('tweetPerMonth.csv', "w", encoding='utf-8', newline='')
    writer = csv.writer(fileout, delimiter=',')

    with open('iot-tweets-2009-2016-topic.tsv', "r", encoding='utf-8') as infile:
        csv_reader = csv.reader(infile, delimiter='\t')
        column = next(csv_reader)
        nbt = 1
        day2 = 'null'
        for row in csv_reader:
            date = row[6].split(' ')
            day1 = date[1] + ' ' + date[5]
            if (day1 == day2):
                nbt = nbt + 1

            else:
                ligne = ["['"+day2+"'", str(nbt)+"],"]
                writer.writerow(ligne)
                nbt = 1

            day2 = day1
            # nbt = nbt + 1
            # print(day)

allMonth()