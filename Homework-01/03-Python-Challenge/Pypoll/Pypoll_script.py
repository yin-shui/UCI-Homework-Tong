# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("election_data.csv")

# List for names and total votes
names = []
total = 0
khan = 0
correy = 0
li = 0
tooley = 0

# Define function
def voter_poll(polldata):
    voterid = str(polldata[0])
    county = str(polldata[1])
    name = names.append(str(polldata[2]))

# Open the CSV
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)

    for row in csvreader:
        voter_poll(row)

# For loop for adding name to counter
for word in names:

    if word == 'Khan':
        khan = khan + 1

    elif word == 'Correy':
        correy = correy + 1

    elif word == 'Li':
        li = li + 1

    elif word == "O'Tooley":
        tooley = tooley + 1

# Variables for calculating percentage
khan_percent = round(khan/ len(names) * 100)
correy_percent = round(correy/ len(names) * 100)
li_percent = round(li/ len(names) * 100)
tooley_percent = round(tooley/ len(names) * 100)

mydict = {
'Khan': khan,
'Correy': correy,
'Li': li,
'Tooley': tooley
}

# output text file
import os

text_output = os.path.join('Pypoll_Analysis.txt')
with open(text_output,'w') as text:


    # Print stats
    text.write('Election Results')
    text.write('------------------')


                #total_months.append(months)
    text.write(f'\nTotal Votes: {len(names)} ')
    text.write('\n------------------')
    text.write(f'\nKhan: %{khan_percent} ({khan}) ')
    text.write(f'\nCorrey: %{correy_percent} ({correy}) ')
    text.write(f'\nLi: %{li_percent} ({li})')
    text.write(f"\nO'Tooley: %{tooley_percent} ({tooley})")
    text.write('\n------------------')
    text.write(f'\nWinner: {max(mydict.items(), key = lambda x: x[1])} ')
    text.write('\n------------------')
