from twarc_csv import CSVConverter


def convert_to_csv(jsonfile_name, csvfile_name):
    print("converting to csv")
    with open(jsonfile_name, "r") as jsonfile:
        with open(csvfile_name, "a", encoding='UTF-8') as csvfile:
            converter = CSVConverter(jsonfile, csvfile)
            converter.process()
