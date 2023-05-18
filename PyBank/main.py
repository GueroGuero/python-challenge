#import module and csv module
import os
import csv

#Making variables for total months, total profits/losses, and average change
total_months = []
total_amount = []
average_change = []

#read csv
file = r"C:\Users\Güero\Desktop\Starter_Code\PyBank\Resources\budget_data.csv"
print(file)

#open csv and use encoding
with open(file, encoding="utf-8") as csvfile:
    csvreader = csv.reader(file, delimiter=",")
    print(csvreader)
    #ignore the headers
    csvheader = next(csvreader)
    #append rows for months and total
    for row in csvreader:
        total_months.append(row[0])
        total_amount.append(int(row[1]))
    #loop through profits for calculation of average change
    for i in range(len(total_amount)-1):
        average_change.append(total_amount[i+1]-total_amount[i])
#variables for greatest incear and decrease
greatest_increase = max(average_change)
greatest_decrease = min(average_change)