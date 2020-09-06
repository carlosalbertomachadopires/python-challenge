


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

  
  {'Correy': 704196, 'Khan': 2218220, 'Li': 492939, "O'Tooley": 105629}
{'Correy': 704196, 'Khan': 2218221, 'Li': 492939, "O'Tooley": 105629}
{'Correy': 704197, 'Khan': 2218221, 'Li': 492939, "O'Tooley": 105629}
{'Correy': 704197, 'Khan': 2218222, 'Li': 492939, "O'Tooley": 105629}
{'Correy': 704197, 'Khan': 2218222, 'Li': 492940, "O'Tooley": 105629}
{'Correy': 704197, 'Khan': 2218223, 'Li': 492940, "O'Tooley": 105629}
{'Correy': 704197, 'Khan': 2218224, 'Li': 492940, "O'Tooley": 105629}
{'Correy': 704198, 'Khan': 2218224, 'Li': 492940, "O'Tooley": 105629}
{'Correy': 704198, 'Khan': 2218225, 'Li': 492940, "O'Tooley": 105629}
{'Correy': 704198, 'Khan': 2218226, 'Li': 492940, "O'Tooley": 105629}
{'Correy': 704199, 'Khan': 2218226, 'Li': 492940, "O'Tooley": 105629}
{'Correy': 704200, 'Khan': 2218226, 'Li': 492940, "O'Tooley": 105629}
{'Correy': 704200, 'Khan': 2218227, 'Li': 492940, "O'Tooley": 105629}
{'Correy': 704200, 'Khan': 2218228, 'Li': 492940, "O'Tooley": 105629}
{'Correy': 704200, 'Khan': 2218229, 'Li': 492940, "O'Tooley": 105629}
{'Correy': 704200, 'Khan': 2218230, 'Li': 492940, "O'Tooley": 105629}
{'Correy': 704200, 'Khan': 2218230, 'Li': 492940, "O'Tooley": 105630}
jupyter@python:~/python-challenge/PyPoll/analysis$ touch README_PyPoll.md
jupyter@python:~/python-challenge/PyPoll/analysis$ 

Khan won with 2_218_230 votes, Correy was in the second place with 704_200 votes, Li was in third_place with 492_940 votes and O'Tooley was the last one with 105_630 votes.

