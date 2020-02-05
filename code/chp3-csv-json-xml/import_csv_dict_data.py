import csv

csvfile = open('data-text.csv', 'rb')
reader = csv.DictReader(csvfile)  #每个数据记录是一个字典

for row in reader:
    print row
