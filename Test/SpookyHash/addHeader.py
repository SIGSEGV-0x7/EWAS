import csv
with open('header.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('header.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['beforeHash','afterHash'])
    w.writerows(data)