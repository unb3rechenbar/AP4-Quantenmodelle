def CSVOpener(data):
    file = open(data)
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    rows = rows[2:]    
    return rows