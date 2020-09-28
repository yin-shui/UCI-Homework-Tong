# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("budget_data.csv")

# List to store months & revenue
total_months = []
num = 86
total_sum = 0
revenue = []
change = []
zip_inc = zip(revenue, total_months)
zip_dec = zip(revenue, total_months)
avgchange = []
#variables for month Change
net_total = 0
total_list = []

# Define function that calculates requirements
def financial_analysis(bankdata):

    months = total_months.append(bankdata[0])
    finacials = revenue.append(int(bankdata[1]))
    profit = int(bankdata[1])



# Open the CSV
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)

    for row in csvreader:
        financial_analysis(row)

# For loop to calculate and store net total values
for i,j in enumerate(revenue[:-1]):
    net_total = total_list.append(revenue[i+1] - revenue[i])

# output text file
import os

text_output = os.path.join('PyBank_Analysis.txt')
with open(text_output,'w') as text:

    # Print stats
    text.write('\nFinancial Analysis')
    text.write('\n------------------')


            #total_months.append(months)
    text.write(f'\nTotal Months: {len(total_months)}')
    text.write(f'\nTotal: {sum(revenue)}')
    text.write(f'\nAverage Change: {round(sum(total_list)/len(total_list),2)}')
    text.write(f'\nGreatest Increase Profits: {max(zip_inc)} ')
    text.write(f'\nGreatest Decrease Profits: {min(zip_dec)} ')
