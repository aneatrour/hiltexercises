#imports csv library, grab it
import csv

# open this file for me in this directory, 'r' means read
#assign a variable (csvfile) to the file itself
with open ('csvs/basic.csv', 'r') as csvfile:

 #go inside csv library and use the reader function on the csvfile, prepare file to be opened
    our_reader = csv.reader(csvfile)
    #for loop for each row, creates a list called names, knows it will be a list due to []
    names = [row for row in our_reader]
#prints out lists of rows including headers
#print(names)
#print second item in names list
#print(names[1]) #prints out row
#prints third thing in second row
#print(names[1][2])
#print(names[2][3])

len(names)

# find longest first name in for loop
for row in names:
    print(len(row[2]))
#find the longest first name
longest = ""
for row in names:
    if len(row[2]) > len(longest):
        longest = row[2]
print(longest)

#construct a new list with only the last names
last_names = [row[1] for row in names]
last_names.reverse()
print(last_names)

#add new data but not written out to file yet
#new_row = [2, 'wayne', 'graham', 'meh']
#names.append(new_row)
#print(names)
#new_row = [3, 'anna', 'neatrour', 'infinity cool']
#names.append(new_row)
#print(names)
#bad example
#a_row = [3, 'fox', 'eliza', 'SO COOL']
#print(names + a_row)
# fout = file output
#csvwriter as new variable, print out rows with certain increments
with open('csvs/practice.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    #range - bottom, top, intervals
    for i in range (0, 100, 10):
        csvwriter.writerow([i, i + 5, i + 10, i + 15, i + 20, i + 25, + i + 30])
