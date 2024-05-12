# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:08:26 2024

@author: Ernie
"""

import os
import csv

# Set up relative Paths
cwd = os.path.abspath(__file__)
dir_name=os.path.dirname(cwd)
election_data_csv=os.path.join(dir_name,'Resources','election_data.csv')
outputpath=os.path.join(dir_name,'analysis','analysis_output.txt')

#Define the function and accept the 'election_data.csv'as its sole parameter
def analysis(election_data_csv):
    with open (election_data_csv, 'r') as file:
        csv_reader = csv.reader(file)
        
        #Skip the header row
        next(csv_reader)
        
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

Total_votes, candidate_votes, candidate_percentage = analysis(election_data_csv)

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
