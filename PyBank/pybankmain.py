
import os
import csv


months =[]
profit_loss_total=[]
profit_loss_change=[]
newlist=[]

csvpathpybank="Resources/budget_data.csv"

with open(csvpathpybank, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    next(csvreader)

#total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
    for row in csvreader:
        months.append(row[0])
        profit_loss_total.append(int(row[1]))
        

a=(len(months))
print("PYBANK Financial Analysis" +'\n')
print("_____________________"+'\n')
print(f"Total number of months is {a}" +'\n')

total=(sum(profit_loss_total))
print(f"Total amount of profit and losses is $ {total}" +'\n')
   
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
for x, y in zip(profit_loss_total[0::],profit_loss_total[1::]):
       profit_loss_change.append(y-x)

avchange=(sum(profit_loss_change)/len(profit_loss_change))      
print(f"Average change over the period $ {avchange}" +'\n')
#excluding base month for new dictionary creation
newmonth=months[1::]

newlist =dict(zip(newmonth,profit_loss_change))


#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

pnlchange = {key: val for key, val in sorted(newlist.items(), key = lambda ele: ele[1])}
revpnlchange = {key: val for key, val in sorted(newlist.items(), key = lambda ele: ele[1], reverse=True)}


a1=(list(pnlchange.items())[0:1])
a2=(list(revpnlchange.items())[0:1])

print(f"The greatest increase in profits (date and amount) over the entire period is {a2}"+'\n')
print(f"The greatest decrease in profits (date and amount) over the entire period is {a1}"+'\n')

fout = "Resources/pybankanalysis.txt"
fo = open(fout, "w")


fo.write(str("PYBANK Financial Analysis" + '\n\n'))
fo.write(str("--------------------------------------------"+ '\n\n'))
fo.write(str("Total number of months is " + str(a)+'\n'))
fo.write(str("Total amount of profit and losses is $")+str(total) +'\n')
fo.write(str("Average change over the period is $")+str(avchange) +'\n')
fo.write(str("The greatest increase in profits (date and amount) over the entire period is")+str(a2) +'\n')
fo.write(str("The greatest decrease in profits (date and amount) over the entire period is")+str(a1) +'\n')

