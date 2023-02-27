# import mariadb as mdb
import mysql.connector as msql
import dbFunctions as dbf

dbHost = 'localhost'
dbPort = 3306
dbUserRoot = 'root'
dbRootPassword = 'toor'
dbName = 'moneyBaggYoooDB'

try:
    connection = msql.connect(host=dbHost, port=dbPort, user=dbUserRoot, password=dbRootPassword, database=dbName)
except(msql.DatabaseError):
    print("Error, not connected")

# def johnnyDropTables(tableName, connCursor):
#     drop = f'DROP TABLE {tableName};'
#     connCursor.execute(drop)

def addEntry(tableName:str, columnNames:list, values:list):
    insert = f'INSERT INTO `{tableName}` (`{columnNames}`) VALUES (`{values}`);'

cursor = connection.cursor()
clientTable = 'clients'
productTable = 'products'
productColumnNames = ['ProductID', 'ProductName', 'ProductPPU', 'ProductSellPrice']
productColumnTypes = ['int', 'varchar(255)', 'float', 'float']
clientColumnNames = ['ClientID', 'ClientFirst', 'ClientBalace']
clientColumnTypes = ['int', 'varchar(255)', 'float']

trialDict = {}

setupQuery = f'CREATE DATABASE `{dbName}`;'

tables = [clientTable, productTable]

clientColumnDict = dbf.createColumnDict(clientColumnNames, clientColumnTypes)
clientColumnNameTypeString = dbf.columnNameTypeString(clientColumnDict)
dbf.createDBTable(connection, cursor, clientTable, clientColumnNameTypeString)
productColumnDict = dbf.createColumnDict(productColumnNames, productColumnTypes)
productColumnNameTypeString = dbf.columnNameTypeString(productColumnDict)
dbf.createDBTable(connection, cursor, productTable, productColumnNameTypeString)

productColumnDict = productTable.createColumnDict(productColumnNames, productColumnTypes)
clientColumnDict = clientTable.createColumnDict(clientColumnNames, clientColumnTypes)

productNameTypeString = productTable.columnNameTypeString(productColumnDict)
clientNameTypeString = clientTable.columnNameTypeString(clientColumnDict)

clientTable.createDBTable(connection, cursor, clientTable, clientNameTypeString)
productTable.createDBTable(connection, cursor, productTable, productNameTypeString)

clientTable.createPrimary(connection, cursor, clientTable, clientColumnNames[0], clientColumnDict)
productTable.createPrimary(connection, cursor, productTable, productColumnNames[0], productColumnDict)

cursor.close()