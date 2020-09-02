# python-challenge

# PyBank

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
        
# Greatest Decrease on Net Profit
        
        Greatest_Decrease_Net_Profit = min(Net_Profit)
        print(f"Greatest Decreasee on Net_Profit: {Greatest_Decrease_Net_Profit}")
        
        
#        Terminal

jupyter@python:~/python-challenge/PyBank/analysis$ python main.csv.py
 Total Months : 1
 Total Months : 2
 Total Months : 3
 Total Months : 4
 Total Months : 5
 Total Months : 6
 Total Months : 7
 Total Months : 8
 Total Months : 9
 Total Months : 10
 Total Months : 11
 Total Months : 12
 Total Months : 13
 Total Months : 14
 Total Months : 15
 Total Months : 16
 Total Months : 17
 Total Months : 18
 Total Months : 19
 Total Months : 20
 Total Months : 21
 Total Months : 22
 Total Months : 23
 Total Months : 24
 Total Months : 25
 Total Months : 26
 Total Months : 27
 Total Months : 28
 Total Months : 29
 Total Months : 30
 Total Months : 31
 Total Months : 32
 Total Months : 33
 Total Months : 34
 Total Months : 35
 Total Months : 36
 Total Months : 37
 Total Months : 38
 Total Months : 39
 Total Months : 40
 Total Months : 41
 Total Months : 42
 Total Months : 43
 Total Months : 44
 Total Months : 45
 Total Months : 46
 Total Months : 47
 Total Months : 48
 Total Months : 49
 Total Months : 50
 Total Months : 51
 Total Months : 52
 Total Months : 53
 Total Months : 54
 Total Months : 55
 Total Months : 56
 Total Months : 57
 Total Months : 58
 Total Months : 59
 Total Months : 60
 Total Months : 61
 Total Months : 62
 Total Months : 63
 Total Months : 64
 Total Months : 65
 Total Months : 66
 Total Months : 67
 Total Months : 68
 Total Months : 69
 Total Months : 70
 Total Months : 71
 Total Months : 72
 Total Months : 73
 Total Months : 74
 Total Months : 75
 Total Months : 76
 Total Months : 77
 Total Months : 78
 Total Months : 79
 Total Months : 80
 Total Months : 81
 Total Months : 82
 Total Months : 83
 Total Months : 84
 Total Months : 85
 Total Months : 86
 
 Total_Net Profit: 38382578
Net Profit Average: 116771.0
Greatest Increase on Net_Profit: 116771
Greatest Decreasee on Net_Profit: 116771
 Total_Net Profit: 38382578
Net Profit Average: -272935.5
Greatest Increase on Net_Profit: 116771
Greatest Decreasee on Net_Profit: -662642
 Total_Net Profit: 38382578
Net Profit Average: -312433.6666666667
Greatest Increase on Net_Profit: 116771
Greatest Decreasee on Net_Profit: -662642
 Total_Net Profit: 38382578
Net Profit Average: -139345.25
Greatest Increase on Net_Profit: 379920
Greatest Decreasee on Net_Profit: -662642
 Total_Net Profit: 38382578
Net Profit Average: -69005.4
Greatest Increase on Net_Profit: 379920
Greatest Decreasee on Net_Profit: -662642
 Total_Net Profit: 38382578
Net Profit Average: 27535.333333333332
Greatest Increase on Net_Profit: 510239
Greatest Decreasee on Net_Profit: -662642
 Total_Net Profit: 38382578
Net Profit Average: -37571.28571428572
Greatest Increase on Net_Profit: 510239
Greatest Decreasee on Net_Profit: -662642
 Total_Net Profit: 38382578
Net Profit Average: -135533.75
Greatest Increase on Net_Profit: 510239
Greatest Decreasee on Net_Profit: -821271
 Total_Net Profit: 38382578
Net Profit Average: -43372.444444444445
Greatest Increase on Net_Profit: 693918
Greatest Decreasee on Net_Profit: -821271
 Total_Net Profit: 38382578
Net Profit Average: 2592.6
Greatest Increase on Net_Profit: 693918
Greatest Decreasee on Net_Profit: -821271
 Total_Net Profit: 38382578
Net Profit Average: -86203.36363636363
Greatest Increase on Net_Profit: 693918
Greatest Decreasee on Net_Profit: -974163
 Total_Net Profit: 38382578
Net Profit Average: -7339.833333333333
Greatest Increase on Net_Profit: 860159
Greatest Decreasee on Net_Profit: -974163
 Total_Net Profit: 38382578
Net Profit Average: -92545.15384615384
Greatest Increase on Net_Profit: 860159
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -12145.642857142857
Greatest Increase on Net_Profit: 1033048
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -4981.4
Greatest Increase on Net_Profit: 1033048
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -23925.875
Greatest Increase on Net_Profit: 1033048
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -16691.882352941175
Greatest Increase on Net_Profit: 1033048
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -44730.833333333336
Greatest Increase on Net_Profit: 1033048
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -10510.78947368421
Greatest Increase on Net_Profit: 1033048
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: 1601.1
Greatest Increase on Net_Profit: 1033048
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -1579.2857142857142
Greatest Increase on Net_Profit: 1033048
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -33449.13636363636
Greatest Increase on Net_Profit: 1033048
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -24256.782608695652
Greatest Increase on Net_Profit: 1033048
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -67643.75
Greatest Increase on Net_Profit: 1033048
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: 12108.36
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -23657.53846153846
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: 10504.962962962964
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -1808.142857142857
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -10245.758620689656
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -12039.4
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1115009
 Total_Net Profit: 38382578
Net Profit Average: -60981.22580645161
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: -12275.6875
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: -2663.878787878788
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: -21285.558823529413
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: -9296.857142857143
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: -14126.416666666666
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: -14767.972972972973
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: -21055.36842105263
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: -10165.358974358975
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: -7557.025
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: 112.09756097560975
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: -1866.7619047619048
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: 3071.1162790697676
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -1529236
 Total_Net Profit: 38382578
Net Profit Average: -46911.568181818184
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -13308.6
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -33823.260869565216
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: 6012.276595744681
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -3863.0416666666665
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -5102.6122448979595
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -875.72
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -5606.686274509804
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -14135.0
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -7921.169811320755
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -3309.685185185185
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -1221.509090909091
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: 5334.982142857143
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: 1393.842105263158
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -4986.482758620689
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: 2044.4237288135594
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: 4530.516666666666
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: 2648.967213114754
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -2908.8870967741937
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -22103.333333333332
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -11082.25
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -12001.36923076923
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -6734.772727272727
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -405.3880597014925
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -4402.279411764706
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -7765.463768115942
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: 1737.357142857143
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -1262.6338028169014
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -3026.1666666666665
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -26962.616438356163
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -14092.297297297297
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -1476.5466666666666
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -5554.934210526316
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -2011.987012987013
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -26047.19230769231
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -3771.9620253164558
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -1242.925
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -9446.901234567902
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -877.6829268292682
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -9721.638554216868
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -8686.357142857143
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
 Total_Net Profit: 38382578
Net Profit Average: -2315.1176470588234
Greatest Increase on Net_Profit: 1926159
Greatest Decreasee on Net_Profit: -2196167
jupyter@python:~/python-challenge/PyBank/analysis$ 