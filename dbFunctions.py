stringNotNull = f'NOT NULL'
stringUnique = f'UNIQUE'
stringAutoIncrement = f'AUTO_INCREMENT'
stringCreateDBTable = f'CREATE TABLE'
stringCreateDB = f'CREATE DATABASE'
stringAlterTable = f'ALTER TABLE'
stringModColumn = f'MODIFY COLUMN'
stringInsertInto = f'INSERT INTO'
stringValues = f'VALUES'
stringDropTable = f'DROP TABLE'
stringDeleteFrom = f'DELETE FROM'
stringWhere = f'WHERE'
stringPrimaryKey = f'PRIMARY KEY'

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
        print(columnNameTypeString)
        return columnNameTypeString

#TESTED WORKING
def createColumnDict(columnNameList:list, columnTypeList:list):
    columnDict = {}
    for i in columnNameList:
        columnDict.update({columnNameList[len(columnDict)]: columnTypeList[len(columnDict)]})
    return columnDict

#TESTED WORKING ON 02/26/2023 @ 20:30
def createDBTable(connection:object, cursor:object, tableName:str, columnNameTypeString:str): 
    command = stringCreateDBTable + ' ' + tableName + ' '
    splitNameType = columnNameTypeString.split(', ')
    primaryKeyAndType = splitNameType[0]
    splitNameType.pop(0)
    command += '(' + primaryKeyAndType + ' ' + stringNotNull + ' ' + stringUnique + ' ' + stringAutoIncrement + ', '

    check = len(splitNameType)
    for i in splitNameType:
        command += i + ', '

    primaryKey = primaryKeyAndType.split(' ')
    primaryKey.pop(1)
    primaryKey = str(primaryKey[0])
    command += stringPrimaryKey + ' (' + primaryKey + '));'

    cursor.execute(command)
    connection.commit()

#WILL NO LONGER BE USED
# def createPrimary(connection:object, cursor:object, tableName:str, primaryColumn:str, columnDict:dict): 
#     command = f'ALTER TABLE {tableName} MODIFY COLUMN {primaryColumn} {columnDict.get(primaryColumn)} PRIMARY KEY ({primaryColumn});'
#     cursor.execute(command)
#     connection.commit()

def addFront(connection:object, cursor:object, tableName:str, values:list): 
    command = f'INSERT INTO clients (ClientFirst, ClientBalance) VALUES (%s,%s)'
    cursor.execute(command, values)
    connection.commit()
    # cursor.execute('SELECT * FROM clients')

def addToBalance(connection:object, cursor:object, tableName:str, clientID:str, balanceAdd:int): 
    command = f'SELECT ClientBalance FROM {tableName} WHERE ClientID={clientID}'
    cursor.execute(command)
    test = cursor.fetchone()
    test = test[0]
    final = test + balanceAdd
    command = f'UPDATE {tableName} SET ClientBalance={final} WHERE ClientID={clientID};'
    cursor.execute(command)
    connection.commit()

def johnnyDropTables(connection:object, cursor:object, tableName):
    command = f'DROP TABLE {tableName};'
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