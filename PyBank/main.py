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

#greatest increase and decrease added to months
#also adding 1 to show max and min after month calculation
greatest_increase_month = average_change.index(max(average_change)) + 1
greatest_decrease_month = average_change.index(min(average_change)) + 1

#print analysis
print("Financial Analysis")
print("-----------------------")
print(f"Total Months : {len(total_months)}")
print(f"Total : ${sum(total_amount)}")

#calculate average change
print(f"Average Change : ${sum(average_change)/len(average_change)}")

#make greatest increase and decrease values as strings and add signs and months
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")

#make text file
analysis = os.path.join("Analysis", "FinancialAnalysis.txt")
with open(analysis, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-------------------")
    file.write("\n")
    file.wrtie(f"Total Months : {len(total_months)}")
    file.write("\n")
    file.write(f"Total : ${sum(total_amount)}")
    file.write("\n")
    file.write(f"Average Change : ${sum(average_change)/len(average_change)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")