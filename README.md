# Python-challenge
## Description
This repository contains two Python projects: PyBank and PyPoll. Each project has its own analysis scripts and associated data files. The purpose of these scripts is to perform analysis of the csv file for the respective project and export the analysis to a .txt file. The PyBank script determines the total number of months in the dataset, calculates the net amount of the "Profits/Losses" column, identifies changes in "Profit/Losses" over the entire period and calculates their average, and finds the greatest increase and decrease in profits (with corresponding dates). The PyPoll script calculates the total number of votes cast, listing all candidates who received votes, calculates the percentage and total number of votes each candidate won, and identifying the candidate who received the most votes and won the election.
## Requirements
The os and csv modules are required for this project
## Installation
Clone the repository: git@github.com:KeeganDavis/python-challenge.git
## Usage
To use this code, run the python script and the data will be analyzed and the results will be exported to a .txt file in the respective analysis folder. 
## Code Source
#### PyBank
-lines 28-33: Find changes in profit/losses over the entire period (https://stackoverflow.com/questions/57055769/how-to-open-a-csv-file-and-go-through-onto-next-line-in-a-loop) \
-line 35: Sum all list elements (https://ioflood.com/blog/python-sum-list-how-to-calculate-the-sum-of-the-elements-in-a-list/) \
-line 35: Round to two decimal places (https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places) \
-lines 47-48: Write file to a text document
