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

def insertRecord(connection:object, cursor:object, tableName:str, columnNameList:list, values:list): 
    # command = f'INSERT INTO {tableName} ({columnNameList}) VALUES ({values});'
    # columnNameList.pop(0)
    values.pop(0)
    # counterItem = len(columnNameList)
    # for i in columnNameList:
    #     if counterItem > 1:
    #         counterString += i + ', '
    #         counterItem -= 1
    #     else:
    #         counterString += i
    # columnListString = counterString

    counterString = ''
    counterItem = len(values)
    for i in values:
        if counterItem > 1:
            counterString += i + ', '
            counterItem -= 1
        else:
            counterString += i
    valueListString = counterString
    
    command = stringInsertInto + ' ' + tableName + ' ' + stringValues + ' (' + valueListString + ');'
     
    cursor.execute(command)
    connection.commit()

def johnnyDropTables(connection:object, cursor:object, tableName):
    command = f'DROP TABLE {tableName};'
    cursor.execute(command)
    connection.commit()

def removeRecord(connection:object, cursor:object, tableName:str, condition:str):
    command = f'DELETE FROM {tableName} WHERE {condition};'
    cursor.execute(command)
    connection.commit()

def updateValues(connection:object, cursor:object, tableName:str, changeColumns:list, valuesList:list, condition:str):
    changeDict = {}
    for i in changeColumns:
        changeDict.update({changeColumns[len(changeDict)]: valuesList[len(changeDict)]})
    print(changeDict)
    dictToString = ''
    for i in changeDict:
        if len(changeDict) + 1 != len(changeColumns):
            dictToString += f'`{i}` = `{changeDict.get()}`, '
        else:
            dictToString += f'`{i}` = `{changeDict.get()}`'
    command = f'UPDATE `{tableName}` SET {dictToString} WHERE {condition};'
    cursor.execute(command)
    connection.commit()