import os
import csv
# from operator import itemgetter, attrgetter
from enum import Enum, unique

path = os.path.join("..", "..", "Instructions", "PyPoll", "Resources", "election_data.csv")

votes_quant = []
candidate_names = []
total_votes = 0
# votes = []


with open(path, "r") as file:
    dict_reader = csv.DictReader(file)
    
    for row in dict_reader:

# The total number of votes cast 
    
        votes_cast = str(row["Voter ID"])
        votes_quant.append(votes_cast)    
        total_quant_votes = len(votes_quant)
        print(total_quant_votes)
        break
        
# A complete list of candidates who received votes
        
    for row in dict_reader:
        
        candidate = (row["Candidate"])
        candidate_names.append(candidate)
        def candidate_with_votes(candidate_names, votes_quant):
            if candidate_names != None and votes_quant == None:
                return False
            else:
                return candidate_names
        result = candidate_with_votes(candidate_names, votes_quant)
        print(f"Candidate with votes: {result}")
        break
           
    for row in dict_reader:
        
# The percentage of votes each candidate won

        print(list(enumerate(candidate_names, start=0)))
        break
            

#         break
#         print(candidate_names)
#         break
        
        
        
        
        county = str(row["County"])
#         print(county)
#         break
        
        
#         candidate_votes = (candidate, votes_cast, county)
#         votes.append(candidate_votes)
#         print(votes)
#         break
#         print(candidate_votes)
#         break
       
    
# A complete list of candidates who received votes
        
#         candidate_sort = sorted(votes, key=lambda votes:[0])
#         print(candidate_sort)
#         candidate_votes = (candidate + votes_cast)
#         print(candidate_votes)
#         break
        
           
        

# The total number of votes each candidate won

# The winner of the election based on popular vote.

