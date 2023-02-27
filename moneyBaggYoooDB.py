# import mariadb as mdb
import mysql.connector as msql
import dbFunctions as dbf

#Init variablees
dbHost = 'localhost'
dbPort = 3306
dbUserRoot = 'root'
dbRootPassword = 'toor'
dbName = 'moneyBaggYoooDB'
clientTable = 'clients'
productTable = 'products'
productColumnNames = ['ProductID', 'ProductName', 'ProductPPU', 'ProductSellPrice']
productColumnTypes = ['int', 'varchar(255)', 'float', 'float']
clientColumnNames = ['ClientID', 'ClientFirst', 'ClientBalace']
clientColumnTypes = ['int', 'varchar(255)', 'float']
tables = [clientTable, productTable]

#Connect to DB if Exists
try:
    connection = msql.connect(host=dbHost, port=dbPort, user=dbUserRoot, password=dbRootPassword, database=dbName)
except(msql.DatabaseError):
    print("Error, not connected")

#Create DB cursor object for interacting with db/running queries
cursor = connection.cursor()

#Create 'clients' column dictionary and the string of both names and types and DB table
clientColumnDict = dbf.createColumnDict(clientColumnNames, clientColumnTypes)
clientColumnNameTypeString = dbf.columnNameTypeString(clientColumnDict)
# dbf.createDBTable(connection, cursor, clientTable, clientColumnNameTypeString)

# #Create 'products' column dictionary and the string of both names and types and DB table
productColumnDict = dbf.createColumnDict(productColumnNames, productColumnTypes)
productColumnNameTypeString = dbf.columnNameTypeString(productColumnDict)
# dbf.createDBTable(connection, cursor, productTable, productColumnNameTypeString)

dbValues = ['John', '80']

#Insert record testing here
dbf.insertRecord(connection, cursor, clientTable, clientColumnNames, dbValues)

#Close DB cursor
cursor.close()