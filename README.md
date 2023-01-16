# Python Challenge

# 1. pybank

* Create empty lists 

* Set file path to read data from

* Skip the header row so that we get correct count and sum

* read through the file rows and create the arrays for month and Profit and loss by using append

* number of months = length of the month array
* sum of the total profit and loss for the period = sum of the array elements
  
* read through files rows looping through row i and row (i+1) and tkae the difference between the two rows 
* create another array that stores the diffs between i and i+1. This array stores the profit and loss change over the months.
*      NOTE  - the length of this array with 1 less than the months array as the first month in the month array is the base month

* average profit and loss change = sum of the profit and loss change array/length of the profit and loss change array  

* create a dictionary by zipping the profit and loss change array and the month array [EXCLUDE THE TOP ROW OF THE MONTH ARRAY]

* sort and reverse sort the dictionary to get the greatest decrease and the greatest increase information
* print all results to txt file and to the terminal


# 2. pypoll

* Create empty lists 

* Set file path to read data from

* Skip the header row so that we get correct count and sum

* read through the file rows and create the arrays for candidates and votes by using append
  
* number of votes = length of the votes array
  
* use set to give a unique list of candidates
  
* count the number of votes per candidate by using "from collections import Counter"
  
* create a dictionary that stores the votes per candidate.
  
* divide the number of votes per candiate by the total number of votes and convert to percentage to get the percentage of votes received by each candidate
  
* Create a dictionary that stores the percentage of votes per candidate

* use reverse sort to get the candidate with the most votes a.k.a the winner

