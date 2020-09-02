import os
import csv


path = os.path.join("..", "..", "Instructions", "PyBank", "Resources", "budget_data.csv")


Months = []
Profit_Losses = []
Avg = []
Net_Profit = []

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    
    header = next(csv_reader)
#     print(header)
    
    for row in csv_reader:
        Months.append(str(row[0]))
        Profit_Losses.append(int(row[1]))
        
# Total Months

        Total_Months = len(Months)
        print(f" Total Months : {Total_Months}")
        
# Total Net Profit 
        
    for i in range(1, len(Profit_Losses)):
        Previous_PL = int(Profit_Losses[i-1])
        Current_PL = int(Profit_Losses[i])
        
        change = (Current_PL - Previous_PL)
        Net_Profit.append(change)
        Total_Net_Profit = sum(Profit_Losses)
        print(f" Total_Net Profit: {Total_Net_Profit}")
        
# Net Profit Average
        
        Total_change = int(sum(Net_Profit))
        Net_Profit_Average = Total_change/len(Net_Profit)
        print(f"Net Profit Average: {Net_Profit_Average}")
        
# Greatest Increase on Net Profit
        Greatest_Increase_Net_Profit = max(Net_Profit)
        print(f"Greatest Increase on Net_Profit: {Greatest_Increase_Net_Profit}")
        
        
        Greatest_Decrease_Net_Profit = min(Net_Profit)
        print(f"Greatest Decreasee on Net_Profit: {Greatest_Decrease_Net_Profit}")
        
        
        