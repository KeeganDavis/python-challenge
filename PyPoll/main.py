import os 
import csv

budget_csv = os.path.join('Resources', 'election_data.csv')

candidate_names = {}
total_votes = 0
candidate_anaylsis = []
highest_percent = 0
winner = None

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] in candidate_names:
            candidate_names[row[2]] += 1
        else:
            candidate_names[row[2]] = 1
            
for name in candidate_names:
     votes = candidate_names[name]
     percentage = round((votes/total_votes) * 100, 3)
     if percentage > highest_percent:
         winner = name
         highest_percent = percentage
     analysis_string = f"{name}: {percentage}% ({votes})"
     candidate_anaylsis.append(analysis_string)
     
final_analysis = (f"Election Results\n"
                  f"-------------------------\n"
                  f"Total Votes: {total_votes}\n"
                  f"-------------------------\n"
                  f"{candidate_anaylsis[0]}\n"
                  f"{candidate_anaylsis[1]}\n"
                  f"{candidate_anaylsis[2]}\n"
                  f"-------------------------\n"
                  f"Winner: {winner}\n"
                  f"-------------------------")

print(final_analysis)

with open('analysis/PyPoll_analysis.txt', 'w') as file:
    file.write(final_analysis)