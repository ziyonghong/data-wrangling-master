import csv

csvfile = open('../../data/chp3/data-text.csv', 'rt')
reader = csv.reader(csvfile)  #返回的是一个数据的列表

for row in reader:
    print (row)
