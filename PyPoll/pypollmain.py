import os
import csv

#creating empty lists

votecount=[]
candidates=[]
votes=[]
votespercent=[]
ucandidates=[]
candpercent=[]
maxvote=[]


csvpathpypoll="Resources/election_data.csv"

with open(csvpathpypoll, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    next(csvreader)

    for row in csvreader:
        votecount.append(int(row[0]))
        candidates.append(row[2])


#The total number of votes cast
x=(len(votecount))


print(f"A total of {x} votes were cast in this election."+'\n')

#A complete list of candidates who received votes
ucandidates=set(candidates)
print(f" Complete list of candidates who received votes in this election : {ucandidates} "+'\n')

#The total number of votes each candidate won

from collections import Counter
a = dict(Counter(candidates))
print("Votes per candiate : "+ '\n')

for k, v in a.items():
    print(str(k) + ' : '+ str(v) + '\n')


#The percentage of votes each candidate won
for i in a:    
    votespercent.append(format((a[i]/x),'2%'))
    candpercent.append(i)

b=dict(zip(candpercent,votespercent))

print("Percentage of votes per candiate:"+'\n')

for k, v in b.items():
    print(str(k) + ' : '+ str(v)  +'\n')

#The winner of the election based on popular vote

sortvote = dict(sorted(b.items(),key=lambda x:x[1], reverse=True))
winner=list(sortvote.keys())[0]
print(f" The winner of this elction by popular votes is {winner}"+'\n')



fout = "Resources/pypollanalysis.txt"
fo = open(fout, "w")

fo.write(str("PYPOLL ANALYSIS")+ '\n\n')
fo.write(str("--------------------------------------------"+ '\n\n'))
fo.write(str("The total number of votes cast =")+ str(x)+'\n\n')
fo.write(str("--------------------------------------------"+ '\n\n'))
fo.write(str("The total number of votes each candidate won"+ '\n\n'))
fo.write(str("--------------------------------------------"+ '\n\n'))
for k, v in a.items():
    fo.write(str(k) + ' >>> '+ str(v) + '\n\n')

fo.write(str("--------------------------------------------"+ '\n\n'))
fo.write(str("The percentage of votes each candidate won"+ '\n\n'))
fo.write(str("--------------------------------------------"+ '\n\n'))
for k, v in b.items():
    fo.write(str(k) + ' >>> '+ str(v) +str("%") +'\n\n')

fo.write(str("--------------------------------------------"+ '\n\n'))
fo.write(str("The winner by popular votes is  =")+ str(winner)+'\n\n')
fo.close()   