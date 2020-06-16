

with open('/Users/andrew/dev/uk-towns/uk-towns-sample.csv') as csvfile:    
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["county"] == "Warwickshire":
            print(row["name"])
            