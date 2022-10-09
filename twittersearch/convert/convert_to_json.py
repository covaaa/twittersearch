import json


def convert_to_json(searched_tweets, jsonfile_name):
    print("converting to json")
    for page in searched_tweets:
        with open(jsonfile_name, "a", encoding='UTF-8') as json_tweets:
            json_tweets.write(json.dumps(page) + "\n")
        print("Wrote a page of results...")
