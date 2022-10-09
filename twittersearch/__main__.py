import os
import datetime

from twittersearch.count import count_tweets
from twittersearch.search import search_tweets
from twittersearch.convert import convert_to_json, convert_to_csv
from twittersearch.format import format_tweets
from twittersearch.output import output_tweets


def main():
    start_year = 2019
    start_month = 6
    start_day = 30
    start_hour = 17
    start_minits = 00
    start_seconds = 0
    start_milliseconds = 0

    end_year = 2019
    end_month = 12
    end_day = 12
    end_hour = 0
    end_minits = 17
    end_seconds = 0
    end_milliseconds = 0

    query = ""
    max_results = 100

    project_path = os.getcwd()

    count_jsonfile_name = "tweet_2019_7_1-2019_12_12_count.jsonl"
    csvfile_name = "tweet_2019_7_1-2019_12_12.csv"
    jsonfile_name = "tweet_2019_7_1-2019_12_12.jsonl"

    output_count_jsonfile_name = "C:\\Users\\developer\\Data\\python_data\\twittersearch_data\\counts\\" # noqa
    output_csvfile_name = "C:\\Users\\developer\\Data\\python_data\\twittersearch_data\\csvtweet\\" # noqa
    output_jsonfile_name = "C:\\Users\\developer\\Data\\python_data\\twittersearch_data\\jsontweet\\" # noqa
    output_trashfile_name = "C:\\Users\\developer\\Data\\python_data\\twittersearch_data\\trashed\\" # noqa

    start_time = datetime.datetime(
        start_year, start_month,
        start_day, start_hour,
        start_minits, start_seconds,
        start_milliseconds,
        datetime.timezone.utc,
        )

    end_time = datetime.datetime(
        end_year, end_month,
        end_day, end_hour,
        end_minits, end_seconds,
        end_milliseconds,
        datetime.timezone.utc,
        )

    input_count_jsonfile = project_path + "\\" + count_jsonfile_name
    input_jsonfile = project_path + "\\" + jsonfile_name
    input_csvfile = project_path + "\\" + csvfile_name

    output_count_jsonfile = output_count_jsonfile_name + count_jsonfile_name
    output_jsonfile = output_jsonfile_name + jsonfile_name
    output_csvfile = output_csvfile_name + csvfile_name
    output_trashfile = output_trashfile_name + csvfile_name

    print("count tweets")
    count_tweets(start_time, end_time, query, count_jsonfile_name)
    print("search tweets")
    searched_tweets = search_tweets(start_time, end_time, query, max_results)
    print("convert to JSON...")
    convert_to_json(searched_tweets, jsonfile_name)
    print("convert to CSV...")
    convert_to_csv(jsonfile_name, csvfile_name)
    print("format CSV file")
    format_tweets(input_csvfile, output_csvfile)
    print("output file")
    output_tweets(
        input_count_jsonfile, output_count_jsonfile,
        input_jsonfile, output_jsonfile,
        input_csvfile, output_trashfile
        )


if __name__ == "__main__":
    main()
