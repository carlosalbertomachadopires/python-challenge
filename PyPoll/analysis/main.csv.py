import os
import csv


path = os.path.join("..", "..", "Instructions", "PyPoll", "Resources", "election_data.csv")

votes_quant = []
candidate_names = []
results = []


with open(path, "r") as file:
    dict_reader = csv.DictReader(file)
    
    for row in dict_reader:

# The total number of votes cast 
    
        votes_cast = str(row["Voter ID"])
        votes_quant.append(votes_cast)    
        total_quant_votes = len(votes_quant)
#         print(f"total number of votes: {total_quant_votes}")
#         break
            
        candidate = (row["Candidate"])
        candidate_names.append(candidate)
        total_quant_candidate = len(candidate)
#         print(total_quant_candidate)
        
# A complete list of candidates who received votes

    for candidate, votes in dict_reader:
        if candidate in results:
            results[candidate] += votes_cast
        else:
            results[candidate] = votes_cast
            
        print(results)
     
        
# The percentage of votes each candidate won


            
    
    
# A complete list of candidates who received votes
        
#         candidate_sort = sorted(votes, key=lambda votes:[0])
#         print(candidate_sort)
#         candidate_votes = (candidate + votes_cast)
#         print(candidate_votes)
#         break
        
           
        

# The total number of votes each candidate won

# The winner of the election based on popular vote.

