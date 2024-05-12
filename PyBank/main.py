# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import csv


# Set up relative Paths
cwd = os.path.abspath(__file__)
dir_name=os.path.dirname(cwd)
budget_data_csv=os.path.join(dir_name,'Resources','budget_data.csv')
outputpath=os.path.join(dir_name,'analysis','analysis_output.txt')



# Define the function and have it accept the 'budget_data' as its sole parameter
def analysis(budget_data_csv):
    with open(budget_data_csv,'r') as file:
        csv_reader = csv.reader(file)
        
        #Skip the header row
        next(csv_reader)
        
        #Initialize variables
        row_count = 0
        total_change = 0
        previous_profit_loss = None
        second_column_sum = 0
        max_increase = float('-inf')
        max_increase_date = None
        max_decrease = float ('inf')
        max_decrease_date = None
        
        #Iterate through each row
        for row in csv_reader:
            row_count += 1
            
            #Convert the second column value to an integer 
            profit_loss = int(row[1])
            second_column_sum += int(row[1])
            
            if previous_profit_loss is not None:
                
                #Calculate the change in profit/loss
                change = profit_loss - previous_profit_loss
                total_change += change
                
                #Check if the change is the maximum increase
                if change > max_increase:
                    max_increase = change
                    max_increase_date = row[0] 
                    
                #Check if the change is the maximum decrease
                if change < max_decrease:
                    max_decrease = change
                    max_decrease_date = row[0]
    
                
            previous_profit_loss = profit_loss
            
        #Calculate the average change
        average_change = total_change / (row_count - 1) #Substract 1 to exclude first row
            
            
    return row_count, second_column_sum, average_change, max_increase, max_increase_date, max_decrease, max_decrease_date

#Unpack the return values of 'analysis'
Total_months, Total_profit, Average_change, Max_increase, Max_increase_date, Max_decrease, Max_decrease_date = analysis(budget_data_csv)


print("Financial Analysis")
print("-" *40) #Create a line of dashes
print(f"Total months : {Total_months}")
print(f"Total : ${Total_profit}")
print(f"Average Change : ${Average_change:.2f}")
print(f"Greatest Increase In Profits: {Max_increase_date} (${Max_increase})")
print(f"Greatest Decrease In Profits: {Max_decrease_date} (${Max_decrease})")