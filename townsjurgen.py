import csv


with open('uk-towns-sample.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        if row["county"] == "Surrey":
            print(row["name"])
