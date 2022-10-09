import pandas as pd


def print_format():
    print("formatting now")


def format_tweets(input_csvfile, output_csvfile):
    print("formatting csv file")
    convertedfile = pd.read_csv(input_csvfile)
    print(convertedfile)
    print(convertedfile.isnull())
    formattedfile = convertedfile.dropna(how='all').dropna(how='all', axis=1)
    print(formattedfile)
    formattedfile.to_csv(output_csvfile)
