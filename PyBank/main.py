import os 
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

months = 0
total_amount = 0
greatest_dec = 0
greatest_inc = 0
monthly_change = []
previous_row = None


with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        months += 1
        total_amount += int(row[1])
        if int(row[1]) > greatest_inc:
            inc_month = row[0]
            greatest_inc = int(row[1])
        if int(row[1]) < greatest_dec:
            dec_month = row[0]
            greatest_dec = int(row[1])
        if previous_row != None:
            change = int(row[1]) - previous_row
            monthly_change.append(change)
            previous_row = int(row[1])
        else:
            previous_row = int(row[1])

average_change = '{:.2f}'.format(sum(monthly_change)/len(monthly_change))

analysis_string = (f"Financial Analysis\n----------------------------\nTotal months: {months}\nTotal: {total_amount}\n"
      f"Average Change: {average_change}\nGreatest Increase in Profits: {inc_month} ({greatest_inc})\nGreatest Decrease in Profits: {dec_month} ({greatest_dec})\n")

print(analysis_string)

with open('analysis/PyBank_analysis.txt', 'w') as file:
    file.write(analysis_string)
    