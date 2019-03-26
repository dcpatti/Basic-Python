import csv                        # Import the CSV Module to load and read the CSV
import os                         # Import the OS module so we can define the file path more easily
Candidates = {}                   # Declare the Dictionary that contains a list of Unique Candidates and their vote
VotesCount = 0                    # Total list of Votes cast, this should equal the total number of lines in the CSV
CandidateCount = 0              # Count of number of Candidates
 
# Open the CSV File for us to process

with open('election_data.csv') as CandidatesFile:
      
       # Create a Reader for the CSV file and set the Comma as the Delimiter

       CandidatesReader = csv.reader(CandidatesFile, delimiter=',')

       # Begin looping over each
       next (CandidatesReader)
       for column in CandidatesReader:

              # Increase the number of votes cast so we can tally the winner later

              VotesCount += 1

              if not column[2] in Candidates:

                     # This user does not exist in the dictionary, so we add him now

                     Candidates[column[2]] = 1

              else:

                     # This user does exist so we increase his vote count

                     Candidates[column[2]] += 1

 

# Get a count of Candidates from the dictionary, so we just need the length as only unique names should exist

CandidateCount = len(Candidates.keys())

 
# Output what we have so far

f = open("results.txt", "w")
f.write("Election Results\n")
print("Candidate Count: " + str(CandidateCount))
f.write("Candidate Count: " + str(CandidateCount)+" \n")

print("Votes Cast: " + str(VotesCount))

f.write("Votes Cast: " + str(VotesCount)+" \n")

# Next we output the Candidates using the Sorted function
# the reverse = true means to sort it in descending order

for Candidate in sorted(Candidates, key=Candidates.get, reverse=True)[:CandidateCount]:
      
       # Format the Vote count to use commas

       VoteCount = "{:,}".format(Candidates[Candidate])

       # Calculate the Vote Percent
       # the {:.2f} means "go to the decimal point and then go 2 places after". the f means the number is a float.
       # https://mkaz.blog/code/python-string-format-cookbook/

       VotePercent = "{:.2f}".format((Candidates[Candidate]/VotesCount) * 100)
     
       #Finally output the Candidate

       print ("Candidate: {0} - Votes: {1} ({2}%)".format(Candidate, VoteCount, VotePercent))
       
       f.write ("Candidate: {0} - Votes: {1} ({2}%)\n".format(Candidate, VoteCount, VotePercent))