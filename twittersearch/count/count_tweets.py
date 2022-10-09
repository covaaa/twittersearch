import os
import json

from twarc import Twarc2


def count_tweets(start_time, end_time, query, count_jsonfile_name):
    print("counting tweets...")
    _token = os.environ.get("BEARER_TOKEN")
    _client = Twarc2(bearer_token=_token)
    count_results = _client.counts_all(
        query=query,
        start_time=start_time,
        end_time=end_time,
    )
    for page in count_results:
        print(json.dumps(page))
        with open(count_jsonfile_name, "a", encoding='UTF-8') as json_tweets: # noqa
            json_tweets.write(json.dumps(page) + "\n")
        print("Wrote a page of results...")
