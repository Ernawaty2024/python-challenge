# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:08:26 2024

@author: Ernie
"""

import os
import csv

# Set up relative Paths
pwf = os.path.abspath(__file__)
pwd = os.path.dirname(pwf)
csvpath = os.path.join(pwd,"Resources","election_data.csv")
export_path = os.path.join(pwd, "analysis", "results.txt")

#Define the function and accept the 'election_data.csv'as its sole parameter
def analysis(csvpath):
    with open (csvpath, 'r') as file:
        csv_reader = csv.reader(file)
        
        #Store the header row
        header = next(csv_reader)
        
        #Initialize variables
        total_votes = 0
        candidate_votes = {}
        
        #Iterate through each row
        for row in csv_reader:
            total_votes += 1
            candidate = row[2]
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1
                
        candidate_percentages = {}
        for candidate, votes in candidate_votes.items():
            percentage = (votes/total_votes) *100
            candidate_percentages[candidate] = percentage
                
                    
    return total_votes, candidate_votes, candidate_percentages

#Unpack the return values of 'analysis'
Total_votes, candidate_votes, candidate_percentage = analysis(csvpath)


#Print analysis to terminal
print(f"Election Results")
print("-"*40)
print(f"Total Votes: {Total_votes}")
print("-"*40)

#Print each candidate and their respective votes and percentages
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentage[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-"*40)

#Find the candidate with the highest number of votes
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner} ")
print("-"*40)

# Export analysis to text file
with open(export_path,"w")as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write("-"*40+ "\n")
    txt_file.write(f"Total Votes: {Total_votes}\n")
    txt_file.write("-"*40+ "\n")
    for candidate, votes in candidate_votes.items():
        percentage = candidate_percentage[candidate]
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txt_file.write("-"*40 + "\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-"*40+ "\n")
