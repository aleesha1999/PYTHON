import csv
with open('C:\python\mytemp.csv','r') as file:
 reader=csv.reader(file)
 for row in reader:
    print(row)
