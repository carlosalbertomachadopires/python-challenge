import os
import csv


path = os.path.join("..", "..", "Instructions", "PyPoll", "Resources", "election_data.csv")

# votes_cast = {}
# candidate = 1
total_votes = 0
# votes = 1

with open(path, "r") as file:
    dict_reader = csv.DictReader(file)
    
    for row in dict_reader:

# The total number of votes cast 
    
        votes_cast = str(row["Voter ID"])
        total_votes +=1     
        print(total_votes)
        break
       
    
# A complete list of candidates who received votes
        
        candidate = (row["Candidate"])
        candidate_votes = (candidate + votes_cast)
        print(candidate_votes)
        break
        
           
        
# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

