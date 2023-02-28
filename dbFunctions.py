# stringNotNull = f'NOT NULL'
# stringUnique = f'UNIQUE'
# stringAutoIncrement = f'AUTO_INCREMENT'
# stringCreateDBTable = f'CREATE TABLE'
# stringCreateDB = f'CREATE DATABASE'
# stringAlterTable = f'ALTER TABLE'
# stringModColumn = f'MODIFY COLUMN'
# stringInsertInto = f'INSERT INTO'
# stringValues = f'VALUES'
# stringDropTable = f'DROP TABLE'
# stringDeleteFrom = f'DELETE FROM'
# stringWhere = f'WHERE'
# stringPrimaryKey = f'PRIMARY KEY'

#TESTED WORKING
def columnNameTypeString(columnDict:dict):   
        columnNameTypeString = ''
        counter = 0
        for i in columnDict:
            if counter + 1 < len(columnDict):
                name = i
                value = columnDict.get(i)
                columnNameTypeString += name + " " + value + ", "
                counter += 1
            else:
                name = i
                value = columnDict.get(i)
                columnNameTypeString += name + " " + value
        counter = 0
        return columnNameTypeString

def createColumnDict(columnNameList:list, columnTypeList:list):
    columnDict = {}
    for i in columnNameList:
        columnDict.update({columnNameList[len(columnDict)]: columnTypeList[len(columnDict)]})
    return columnDict

def createDatabase(connection:object, cursor:object, dbName:str):
    command = f'CREATE DATABASE {dbName}'
    cursor.execute(command)
    connection.commit()

def createTable(connection:object, cursor:object, columnNameType:str, tableName:str):
    command = f'CREATE TABLE {tableName} ({columnNameType});'
    cursor.execute(command)
    connection.commit()


#Client Table functions
def addFront(connection:object, cursor:object, values:list): 
    command = f'INSERT INTO clients (ClientFirst, ClientLast, ClientBalance) VALUES (%s,%s,%s)'
    cursor.execute(command, values)
    connection.commit()

def addToBalance(connection:object, cursor:object, tableName:str, clientID:str, balanceAdd:int): 
    command = f'SELECT ClientBalance FROM {tableName} WHERE ClientID={clientID}'
    cursor.execute(command)
    test = cursor.fetchone()
    test = test[0]
    final = test + balanceAdd
    command = f'UPDATE {tableName} SET ClientBalance={final} WHERE ClientID={clientID};'
    cursor.execute(command)
    connection.commit()

def makePayment(connection:object, cursor:object, tableName:str, clientID:int, *clientFirst:str, repayAmount:int):
    command = f'SELECT ClientBalance FROM {tableName} WHERE ClientID={clientID}'
    cursor.execute(command)
    test = cursor.fetchone()
    test = test[0]
    final = test - repayAmount
    command = f'UPDATE {tableName} SET ClientBalance={final} WHERE ClientID={clientID};'
    cursor.execute(command)
    connection.commit()


#Product Table Functions
def addProducts(connection:object, cursor:object, values:list):
    command = f'INSERT INTO products (ProductName, ProductCostPerUnit, ProductSalePerUnit, ProductTotalAmount) VALUES (%s,%s,%s,%s)'
    cursor.execute(command, values)
    connection.commit()

def johnnyDropTables(connection:object, cursor:object, tableName):
    command = f'DROP TABLE {tableName};'
    cursor.execute(command)
    connection.commit()