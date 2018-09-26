#ShowMeTheCode -- Sajed Nahian & Mohammed Uddin
#SoftDev1 pd6
#K06 StI/O: Divine your Destiny!
#2018-9-08

import csv
import random;

headings = {}
occupationsDictionary = {}
totalPercentage = 0;

def processFile (fileName):
    global totalPercentage
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        row_count = sum(1 for line in open(fileName))
        # print(row_count);
        for row in csv_reader:
            if line_count == 0:
                headings[0] = row[0] 
                headings[1] = row[1] 
                line_count += 1
            elif line_count == row_count - 1:
                # Record the total percentage found on last row
                totalPercentage = float(row[1]) 
            else:
                # Add row information into dictionary
                job_class = row[0].replace("\"", "")
                percentage = float(row[1])
                occupationsDictionary[job_class] = percentage;
                line_count += 1

def pickRandomOccupation ():
    # pick random number in range of the total percentage
    randomNum = random.uniform(0.0, totalPercentage)
    cur = 0
    for occupation in occupationsDictionary:
        # if the randomNum in in the range corresponding the occuption's percentage, return it
        cur += occupationsDictionary[occupation]
        if randomNum <= cur:
            return occupation

processFile('static/occupations.csv')
pickedOccupation = pickRandomOccupation()
print (pickedOccupation)