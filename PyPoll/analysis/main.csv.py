import os
import csv

path=os.path.join("..","..","Instructions", "PyPoll", "Resources", "election_data.csv")

vote = []
candidates = []
county = []
results = {}



with open(path, "r") as file:
    csv_reader = csv.reader(file)
    
    print(dir(csv_reader))
    
    header = next(csv_reader)
    print(header)
                 
    
    for row in csv_reader:
        vote.append(row[0])
#         print(vote)
        total_vote = len(vote)
        print(total_vote)
        break
    for vote, places, candidate in csv_reader:
        if candidate in results:
            results[candidate] += 1
        else:
            results[candidate] = 1
        print(results)
                
#         Percentage = total_vote / results[candidate]    

   
      