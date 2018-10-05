#WorryAboutThoseComments - Sajed Nahian & Matthew Ming
#SoftDev1 pd6
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def createTableFromCSV(fileName, tableName, columnTypes):
	with open(fileName) as csvfile:
		reader = csv.DictReader(csvfile)
		createTable(reader, tableName, columnTypes)
		

def createTable(info, tableName, columnTypes):
	commandArgs = "("
	colTypes = []
	for name in columnTypes:
		commandArgs += name + " " + columnTypes[name] + ","
		colTypes.append(columnTypes[name])
	commandArgs = commandArgs[:-1]
	# print(colTypes)
	commandArgs += ")"
	# print ("CREATE TABLE " + tableName + " "+ commandArgs)
	c.execute("CREATE TABLE " + tableName + " "+ commandArgs)
	# c.execute("SELECT * FROM " + tableName)
	for od in info:
		i = 0
		fieldValueArg = "("
		for key in od:
			if colTypes[i] == "INTEGER":
				fieldValueArg += od[key] + ","
			else: 
				fieldValueArg += "'" + od[key] + "'" + ","
			i += 1
		fieldValueArg = fieldValueArg[:-1]
		fieldValueArg += ")"
		# print ("INSERT INTO " + tableName + " VALUES " + fieldValueArg)
		c.execute("INSERT INTO " + tableName + " VALUES " + fieldValueArg)

def closeDB ():
	db.commit() #save changes
	db.close()  #close database

coursesHeader = {"code":"TEXT","grades":"INTEGER","id":"INTEGER"}
createTableFromCSV("courses.csv", "coursestable", coursesHeader)

peepsHeader = {"name": "TEXT", "age": "INTEGER", "id": "INTEGER"}
createTableFromCSV("peeps.csv", "peepstable", peepsHeader)

occupationsHeader = {"jobclass": "TEXT", "percentage":"INTEGER"}
createTableFromCSV("occupations.csv", "occupationstable", occupationsHeader)

closeDB()
