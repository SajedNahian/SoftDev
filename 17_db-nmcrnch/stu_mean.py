#What - Jeffrey Wu and Sajed Nahian
#SoftDev1 pd6
#K17 Average
#2018-10-06

import sqlite3   #enable control of an sqlite database

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def closeDB ():
	db.commit() #save changes
	db.close()  #close database

def getQueryResult (query):
  c.execute(query)
  return c.fetchall()

def createTable (tableName, tableHeader):
  commandsArgs = "("
  for name in tableHeader:
    commandsArgs += "{0} {1},".format(name, tableHeader[name])
  commandsArgs = commandsArgs[:-1]
  commandsArgs += ")"
  c.execute("CREATE TABLE {0} {1}".format(tableName, commandsArgs))

studentIDs = getQueryResult("SELECT id FROM 'peepstable'")

tableHeader = {'name': 'TEXT', 'id': 'INTEGER', 'average': 'NUMERIC'}
createTable('peeps_avg', tableHeader)

for idNo in studentIDs:
    print("SELECT grades FROM 'coursestable' WHERE id = " + str(idNo[0]))
    grades = getQueryResult("SELECT grades FROM 'coursestable' WHERE id = " + str(idNo[0]))
    gradeSum = 0
    for grade in grades:
        gradeSum += grade[0]
    name = getQueryResult("SELECT name FROM 'peepstable' WHERE id = " + str(idNo[0]))[0][0]
    print(name)
    c.execute("INSERT INTO peeps_avg VALUES('{0}',{1},{2})".format(name,
                                                                   str(idNo[0]),
                                                                   str(gradeSum/3)))

peeps = getQueryResult('SELECT * from peeps_avg')
for rec in peeps:
    print(rec)
closeDB();