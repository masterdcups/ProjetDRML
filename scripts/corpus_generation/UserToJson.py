# !/usr/bin/env python
# coding: utf-8


import json
import glob


def mergeJson():
    data = {}
    result = []
    for f in glob.glob("resUser*.json"):
        with open(f, "r") as infile:
            tmp_json = json.load(infile)['users']
            result.extend(tmp_json)

    data['users'] = result
    with open("resUserComplet.json", "w") as outfile:
        json.dump(data,outfile)

def removeDuplicates():
        with open('resUserComplet.json') as fp:
            ds = json.load(fp)  # this file contains the json

            users = {}

            for record in ds:
                id = int(record["user_id"])
                if id not in users:
                    users[id] = record

            with open('resUserFinal.json', 'w') as outfile:
                json.dump(users, outfile)



def extractUser():

    filename = 'inutile/resfinalbistrois4'

    users = {'users': []}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            user = {}

            # convert to a valid json format
            #         line = line.replace("\"","\\\"")
            #         line = line.replace("'","\"")
            line = line.replace("True", "true")
            line = line.replace("False", "false")
            line = line.replace("None", "null")
            fields = line.split(',')

            for field in fields:
                text = field.strip()
                if text[0:13] == "'user': {'id'":
                    user['user_id'] = text[14:].strip()
                    break

            for field in fields:
                text = field.strip()
                if text[0:13] == "'screen_name'":
                    user['user_name'] = text[14:].strip()
                    break

            users['users'].append(user)

    # json_data = json.dumps(tweets)
    with open('resUser4.json', 'w') as outfile:
        json.dump(users, outfile)

def main():
    #extractUser()
    #mergeJson()
    removeDuplicates()


if __name__ == "__main__":
    main()


