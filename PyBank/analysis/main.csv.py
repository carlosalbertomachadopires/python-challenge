import os
import csv


path = os.path.join("..", "..", "Instructions", "PyBank", "Resources", "budget_data.csv")

months = 0

with open(path, "r") as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        months = months + 1
    print("Months Count:", months)
    
            
       
#         changes = []
#         for i in range(1, len(data)):
#             last_period_row = data[i-1]
#             current_period_row = data[i]
        
#             change = (last_period_row + current_period_row)
        
#             changes.append(change)

      
# #         print(changes)
        

# header = PyBank.readline()

# data = print([element.strip().split(",") for element in PyBank])

# print(new_list)

# count = len(new_list)

# new_list[0]

# total = 0
# for e in new_list:
#     total = total + 1

# #     print(type(PyBank))
# new_list[0][1]
    
# #     header = file.readline()
# # #     print("This is the header")
# # #     print(header)
    
# #     data = file.readlines()
# # # #     data = int(data)
# # # #     print("This is the data")
# # #     print(type(data))
# # #     print(data)
    
    
# # #      print([element.strip().split(" ")for element in data])
    
#       dict_reader = csv.DictReader(file)
#       for row in dict_reader:
#         print(dict(row))
               
