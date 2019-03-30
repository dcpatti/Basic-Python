#Load the CSV reader and the OS path interpreter
import os
import csv

 #Open and read the file. The first row is a header

with open('budget_data.csv', 'r') as csvfile:
    next(csvfile)
    readCSV = csv.reader(csvfile, delimiter=',')
    num_lines = 0
    total = 0
    PLAverage = 0
    PLHighest = 0
    PLLowest = 0
    HighDate = ''
    LowDate = ''

    for column in readCSV:

        
#The total number of months included in the dataset
        num_lines += 1  
#The net total amount of "Profit/Losses" over the entire period
        total += int(column[1])
#Average of the changes in the profit/losses over the entire period
#Has to be done outside the iteration or else it recalculates on every row and gets too big

 
#Check the value to see if it is the greatest increase in profits (date and amount) over the entire period
#If not, check if it is the greatest decrease in losses (date and amount) over the entire period
#If either condition is met, put the value into the variable along with the value of the month

        if int(column[1]) > PLHighest:
            PLHighest = int(column[1])
            HighDate = str(column[0])
        elif int(column[1]) < PLLowest:
            PLLowest = int(column[1])
            LowDate = str(column[0])
 #Do all the writing and printing  
 #First open a file to hold the output

f = open("budget_results.txt", "w")
f.write("Budget Info\n")
#clean up the formatting of the Average
PLAverage = "{:.2f}".format((total/num_lines))
print("Number of Months: " + str(num_lines))  
    
f.write("Number of Months: " + str(num_lines)+" \n") 

print ("Total Profit or Loss: " + str(total))
f.write ("Total Profit or Loss: " + str(total)+" \n") 
print ("Average Profit/Loss  " + str(PLAverage))
f.write ("Average Profit/Loss  " + str(PLAverage)+" \n") 
print ("Highest Increase  " + HighDate + "  " + str(PLHighest))
f.write("Highest Increase  " + HighDate + "  " + str(PLHighest)+" \n") 
print ("Highest Decrease  " + LowDate  + "  " + str(PLLowest) )
f.write ("Highest Decrease  " + LowDate  + "  " + str(PLLowest)+" \n") 



