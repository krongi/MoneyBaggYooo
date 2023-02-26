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

# productTableColumnsCreate = 'ProductID int NOT NULL UNIQUE AUTO_INCREMENT, ProductName varchar(255), ProductPPU float, ProductSellPrice float'
# clientTableColumnsCreate = 'ClientID int NOT NULL UNIQUE AUTO_INCREMENT, ClientFirst varchar(255), ClientBalance float'

# clientTableCreate = f'CREATE TABLE {clientTable} ({clientTableColumnsCreate});'
# productTableCreate = f'CREATE TABLE {productTable} ({productTableColumnsCreate});'

setupQuery = f'CREATE DATABASE `{dbName}`;'

tables = [clientTable, productTable]
# queries = [clientTableCreate, productTableCreate]

# for i in tables:
#     johnnyDropTables(i, cursor)
clientColumnDict = dbf.createColumnDict(clientColumnNames, clientColumnTypes)
clientColumnNameTypeString = dbf.columnNameTypeString(clientColumnDict)
dbf.createDBTable(connection, cursor, clientTable, clientColumnNameTypeString)
productColumnDict = dbf.createColumnDict(productColumnNames, productColumnTypes)
productColumnNameTypeString = dbf.columnNameTypeString(productColumnDict)
dbf.createDBTable(connection, cursor, productTable, productColumnNameTypeString)
# clientTable = scratch.TableSetup(connection, cursor, clientTable, clientColumnNames[0], clientColumnNames, clientColumnTypes)
# productTable = scratch.TableSetup(connection, cursor, productTable, productColumnNames[0], productColumnNames, productColumnTypes)

productColumnDict = productTable.createColumnDict(productColumnNames, productColumnTypes)
clientColumnDict = clientTable.createColumnDict(clientColumnNames, clientColumnTypes)

productNameTypeString = productTable.columnNameTypeString(productColumnDict)
clientNameTypeString = clientTable.columnNameTypeString(clientColumnDict)

clientTable.createDBTable(connection, cursor, clientTable, clientNameTypeString)
productTable.createDBTable(connection, cursor, productTable, productNameTypeString)

clientTable.createPrimary(connection, cursor, clientTable, clientColumnNames[0], clientColumnDict)
productTable.createPrimary(connection, cursor, productTable, productColumnNames[0], productColumnDict)

cursor.close()