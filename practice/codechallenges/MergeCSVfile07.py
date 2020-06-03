import csv

def merge_csv(csv_list, output_path):
    #build list with all fielnames
    fieldnames = list()
    for file in csv_list:
        with open(file, 'r') as input_csv:
            fn = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(x for x in fn if x not in fieldnames)

    # write data to output file based on field names
    with open(output_path, 'w', newline='') as output__csv:
        writer = csv.DictWriter(output__csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)


merge_csv(['D:\\test\\france.csv', 'D:\\test\\poland.csv'], 'D:\\test\\all.csv')
