# import mariadb as mdb
import mysql.connector as msql
import scratch

dbHost = 'localhost'
dbPort = 3306
dbUserRoot = 'root'
dbRootPassword = 'toor'
dbName = 'moneyBaggYoooDB'

try:
    connection = msql.connect(host=dbHost, port=dbPort, user=dbUserRoot, password=dbRootPassword, database=dbName)
except(msql.DatabaseError):
    print("Error, not connected")

def johnnyDropTables(tableName, connCursor):
    drop = f'DROP TABLE {tableName};'
    connCursor.execute(drop)

def addEntry(tableName:str, columnNames:list, values:list):
    insert = f'INSERT INTO `{tableName}` (`{columnNames}`) VALUES (`{values}`);'

cursor = connection.cursor()
clientTable = 'clients'
productTable = 'product'
productColumnNames = ['ProductID', 'ProductName', 'ProductPPU', 'ProductSellPrice']
productColumnTypes = ['int', 'varchar(255)', 'float', 'float']
clientColumnNames = ['ClientID', 'ClientFirst', 'ClientBalace']
clientColumnTypes = ['int', 'varchar(255)', 'float']


productTableColumnsCreate = 'ProductID int NOT NULL UNIQUE AUTO_INCREMENT, ProductName varchar(255), ProductPPU float, ProductSellPrice float'
clientTableColumnsCreate = 'ClientID int NOT NULL UNIQUE AUTO_INCREMENT, ClientFirst varchar(255), ClientBalance float'

clientTableCreate = f'CREATE TABLE {clientTable} ({clientTableColumnsCreate});'
productTableCreate = f'CREATE TABLE {productTable} ({productTableColumnsCreate});'

setupQuery = f'CREATE DATABASE `{dbName}`;'

tables = [clientTable, productTable]
queries = [clientTableCreate, productTableCreate]

clientTable = scratch.TableSetup(cursor, clientTable, clientColumnNames[0], clientColumnNames, clientColumnTypes)
productTable = scratch.TableSetup(cursor, productTable, productColumnNames[0], productColumnNames, productColumnTypes)


for i in queries:
    result = None
    # johnnyDropTables(i, cursor)
    # johnnyDropTables
    cursor.execute(i)
    print(i)
    print(cursor)
    result = cursor.fetchall()
# cursor.close()