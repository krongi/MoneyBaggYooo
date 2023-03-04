# import mariadb as mdb
import mysql.connector as msql
import dbFunctions as dbf

#Init variablees
# dbHost = 'localhost'
# dbPort = 3306
# dbUserRoot = 'root'
# dbRootPassword = 'toor'
# dbName = 'moneybaggyooodb'
# clientTable = 'clients'
# productTable = 'products'
# productColumnNames = ['ProductID', 'ProductName', 'ProductPPU', 'ProductSellPrice']
# productColumnTypes = ['int', 'varchar(255)', 'float', 'float']
# clientColumnNames = ['ClientID', 'ClientFirst', 'ClientBalance']
# clientColumnTypes = ['int', 'varchar(255)', 'float']
# clientColumnNameTypeString = 'ClientID int NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT, ClientFirst varchar(255), ClientLast varchar(255), ClientBalance float'
# productColumnNameTypeString = 'ProductID int NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT, ProductName varchar(255), ProductCostPerUnit float, ProductPricePerUnit float, ProductTotalAmount float'
# tables = [clientTable, productTable]

#Connect to DB if Exists
def connection():
    dbHost = 'localhost'
    dbPort = 3306
    dbUserRoot = 'root'
    dbRootPassword = 'toor'
    dbName = 'moneybaggyooodb'
    clientTable = 'clients'
    productTable = 'products'
    assetTable = 'assets'
    # productColumnNames = ['ProductID', 'ProductName', 'ProductPPU', 'ProductSellPrice']
    # productColumnTypes = ['int', 'varchar(255)', 'float', 'float']
    # clientColumnNames = ['ClientID', 'ClientFirst', 'ClientBalance']
    # clientColumnTypes = ['int', 'varchar(255)', 'float']
    assetColumnNameTypeString = 'AssetID int NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT, AssetType varchar(255), AssetName varchar(255), AssetValue int'
    clientColumnNameTypeString = 'ClientID int NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT, ClientFirst varchar(255), ClientLast varchar(255), ClientBalance int'
    productColumnNameTypeString = 'ProductID int NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT, ProductName varchar(255), ProductCostPerUnit int, ProductPricePerUnit int, ProductTotalAmount int'
    tables = [clientTable, productTable]
    try:
        connection = msql.connect(host=dbHost, port=dbPort, user=dbUserRoot, password=dbRootPassword)#, database=dbName)
        cursor = connection.cursor(buffered=True)
    except(msql.DatabaseError):
        print("Error, not connected")

    try:
        dbf.createDatabase(connection, cursor, dbName)
    except (msql.DatabaseError):
        print('DB already exists')

    try:
        connection = msql.connect(host=dbHost, port=dbPort, user=dbUserRoot, password=dbRootPassword, database=dbName)
        cursor = connection.cursor(buffered=True)
    except(msql.DatabaseError):
        print('Unable to connect to ' + dbName)

    try:
        dbf.createTable(connection, cursor, clientColumnNameTypeString, clientTable)
        clientTableCreated=False
    except:
        msql.ProgrammingError(errno=1050)
        print("Clients table already exists")
        clientTableCreated=True

    try:
        dbf.createTable(connection, cursor, productColumnNameTypeString, productTable)
        productTableCreated=False
    except:
        msql.ProgrammingError(errno=1050)
        print("Products table already exists")
        productTableCreated=True

    try:
        dbf.createTable(connection, cursor, assetColumnNameTypeString, assetTable)
        assetTableCreated=False
    except:
        msql.ProgrammingError(errno=1050)
        print("Products table already exists")
        assetTableCreated=True
    
    if clientTableCreated != True:
        for i in clientTupleList:
            dbf.addFront(connection, cursor, i)

    if productTableCreated != True:        
        for i in productTupleList:
            dbf.addProducts(connection, cursor, i)

    if assetTableCreated != True:        
        for i in assetTupleList:
            dbf.addAssets(connection, cursor, i)

    return [connection, cursor]

assetTupleList = [('Liquid', 'Cash', '200')]
clientTupleList = [('John', 'Paz', '100'), ('Chico', 'Marino', '50'), ('Mike', 'Hummer', '200'), ('Walt', 'MindyMan', '50'), ('Stone', 'Lingo', '70'), ('Striker', 'VonFireworkin', '60'), ('Lee', 'Redard', '40'), ('Alexa', 'TashiFriend', '20')]
productTupleList = [('Go Green Certificate', '4.28', '10.00', '28'), ('Software License', '32.14', '100.00', '20'), ('Software Hardening License', '32.14', '120.00', '0'), ('Modified Software License', '21.53', '80.00', '0')]

# for i in clientTupleList:
#     dbf.addFront(connection, cursor, i)

# for i in productTupleList:
#     dbf.addProducts(connection, cursor, i)

# dbf.reduceProductTotal(connection, cursor, 'ProductTotalAmount', '80', 'Software License')

# dbf.changeProductCost(connection, cursor, 'Go Green Certificate', '2.00')
# dbf.changeProductPrice(connection, cursor, 'Go Green Certificate', '130.00')

# command = f'SELECT ClientID FROM {clientTable} WHERE ClientFirst=\'Chico\''
# cursor.execute(command)
# cid = cursor.fetchone()
# cid = cid[0]
# dbf.addToBalance(connection, cursor, clientTable, cid, 20)
#Create 'clients' column dictionary and the string of both names and types and DB table
# clientColumnDict = dbf.createColumnDict(clientColumnNames, clientColumnTypes)
# clientColumnNameTypeString = dbf.columnNameTypeString(clientColumnDict)

# #Create 'products' column dictionary and the string of both names and types and DB table
# productColumnDict = dbf.createColumnDict(productColumnNames, productColumnTypes)
# productColumnNameTypeString = dbf.columnNameTypeString(productColumnDict)

#Close DB cursor
# cursor.close()