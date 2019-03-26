
#Load the CSV reader and the OS path interpreter
import os
import csv


#poll_csv = os.path.join("..", "python-challenge","py-bank","election_subset.csv")
#Open and read the file. The first row is a header

with open('election_subset.csv', 'r') as csvfile:
    next(csvfile)
    readCSV = csv.reader(csvfile, delimiter=',')
    num_lines = 0
   
 #Create a dictionary to hold the candidates
    Candidates = {}
    #curly brackets means dictionary and square means list
    for column in readCSV:
        num_lines += 1  
        if column[2] not in Candidates:
         #If the candidate name is not in the column, add it to the dictionary as the key and set the value to 1)
         Candidates[column[2]] = 1
        else: #if it's already there, just increase the value
            Candidates[column[2]] += 1
for key,value in Candidates.items():
    print(Candidates)
    print("Total Votes Cast :  " + str(num_lines))
