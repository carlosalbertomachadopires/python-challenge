import os
import csv


path = os.path.join("..", "..", "Instructions", "PyBank", "Resources", "budget_data.csv")

with open(path, "r") as file:
    
    header = file.readLine()
    print("This the header")
    print(header)
    