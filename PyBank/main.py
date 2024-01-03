import os 
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

# initialize variables
months = 0
total_amount = 0
greatest_dec = 0
greatest_inc = 0
monthly_change = []
previous_row = None

# read csv and store header
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

# loops through csv and counts number of months and finds total profit or loss
    for row in csvreader:
        months += 1
        total_amount += int(row[1])
        # finds the changes in "Profit/Losses" over the entire period
        if previous_row != None:
            change = int(row[1]) - previous_row
            monthly_change.append(change)
            # find month and greatest profit inc
            if change > greatest_inc:
                inc_month = row[0]
                greatest_inc = change
            # find month and greatest profit dec
            if change < greatest_dec:
                dec_month = row[0]
                greatest_dec = change
            previous_row = int(row[1])
        else:
            previous_row = int(row[1])

# finds the average changes over the entire period
average_change = '{:.2f}'.format(sum(monthly_change)/len(monthly_change))

# final f-string to print and add to .txt file
analysis_string = (f"Financial Analysis\n----------------------------\nTotal months: {months}\nTotal: ${total_amount}\n"
      f"Average Change: ${average_change}\nGreatest Increase in Profits: {inc_month} (${greatest_inc})\nGreatest Decrease in Profits: {dec_month} (${greatest_dec})\n")

print(analysis_string)

# write f-string to .txt file
with open('analysis/PyBank_analysis.txt', 'w') as file:
    file.write(analysis_string)
    