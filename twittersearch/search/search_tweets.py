import os

from twarc import Twarc2


def print_search():
    print("search now")


def search_tweets(start_time, end_time, query, max_results):
    _token = os.environ.get("BEARER_TOKEN")
    _client = Twarc2(bearer_token=_token)

    print(f"searching for \"{query}\" tweets from {start_time} to {end_time}...")
    search_results = _client.search_all(
        query=query,
        start_time=start_time,
        end_time=end_time,
        max_results=max_results,
        )
    return search_results
