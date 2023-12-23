import os 
import csv

budget_csv = os.path.join('Resources', 'election_data.csv')

# initialize all variables
candidate_names = {}
total_votes = 0
candidate_anaylsis = []
highest_percent = 0
winner = None

# read csv
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # store header
    header = next(csvreader)

    # loop through csv and tally total votes. Adds name to the dictionary if it does not exist and adds one to the value of the candidate to keep track of votes per candidate
    for row in csvreader:
        total_votes += 1
        if row[2] in candidate_names:
            candidate_names[row[2]] += 1
        else:
            candidate_names[row[2]] = 1

# Loops through the dictionary and calculates the % of total votes. Checks to see which candidate has the highest % and stores them in winner.             
for name in candidate_names:
     votes = candidate_names[name]
     percentage = round((votes/total_votes) * 100, 3)
     if percentage > highest_percent:
         winner = name
         highest_percent = percentage
    # adds f-string with candidate name, % of votes, and total # of votes
     analysis_string = f"{name}: {percentage}% ({votes})"
     candidate_anaylsis.append(analysis_string)

# Final f-string to print     
final_analysis = (f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n"
                  f"{candidate_anaylsis[0]}\n{candidate_anaylsis[1]}\n{candidate_anaylsis[2]}\n-------------------------\n"
                  f"Winner: {winner}\n-------------------------")

print(final_analysis)

# Writes the final f-string to .txt file
with open('analysis/PyPoll_analysis.txt', 'w') as file:
    file.write(final_analysis)