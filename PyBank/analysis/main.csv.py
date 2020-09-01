import os
import csv


path = os.path.join("..", "..", "Instructions", "PyBank", "Resources", "budget_data.csv")

# with open(path, "r") as file:
#     header = file.readline()
#     print("This is the header")
#     print(header)
    
#     data = file.readlines()    
#     print("This is the data")
#     print(data)
    
#     print([row.strip().split(",") for row in data])
    
with open(path, "r") as file:
    csv_reader = csv.reader(file)
    
    header = next(csv_reader)
    print(header)
    
    data = list(csv_reader)
    print(data)
    
   
    changes = []
    for i in range(1, len(data)):
        last_period_row = data[i-1]
        current_period_row = data [i]
        
        change = i + 1       
        changes.append(change)
        print(f" Total Months: {change}")
        
  


# with open(path, "r") as file:
#     dict_reader = csv.DictReader(file)
#     for row in dict_reader:
#         print(dict(row))