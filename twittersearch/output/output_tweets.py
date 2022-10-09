import os


def print_output():
    print("output now")


def output_tweets(
    input_count_jsonfile, output_count_jsonfile,
    input_jsonfile, output_jsonfile,
    input_csvfile, output_trashfile
        ):
    os.replace(input_count_jsonfile, output_count_jsonfile)
    os.replace(input_jsonfile, output_jsonfile)
    os.replace(input_csvfile, output_trashfile)
