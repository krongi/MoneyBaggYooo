import mysql.connector
class TableSetup():
    def __init__(self, connection, connectionCursor, tableName, primaryColumn, columnNameList, columnTypeList) -> None:
        self.tableName = tableName
        self.columnNameList = columnNameList
        self.columnType = columnTypeList
        self.primaryColumn = primaryColumn
        self.connection = connectionCursor
        self.msqlConnection = connection

        # self.columnDict = {} 
        # self.counter = 0

        # for i in self.columnNameList:
        #     self.columnDict.update({str(self.columnNameList[counter]): str(columnTypeList[counter])})
            # self.counter += 1
        columnDict = self.createColumnDict(self.columnNameList, self.columnType)
        firstString = f'{primaryColumn} {columnDict.get(primaryColumn)} NOT NULL UNIQUE AUTO_INCREMENT, '
        primaryString = self.columnNameTypeString(columnDict)
        primaryString = primaryString.split(', ')
        primaryString.pop(0)
        lastString = f'PRIMARY KEY ({primaryColumn});'
        for i in primaryString: 
            finalString += i
            return 
        
    def columnNameTypeString(self, columnDict:dict):   
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

    def createColumnDict(self, columnNameList:list, columnTypeList:list):
        columnDict = {}
        for i in columnNameList:
            columnDict.update({columnNameList[len(columnDict)]: columnTypeList[len(columnDict)]})
        return columnDict
    
    def createDBTable(self, connection:object, cursor:object, tableName:str, columnNameTypeString:str): 
        command = f'CREATE TABLE {tableName} ({columnNameTypeString});'
        cursor.execute(command)
        connection.commit()

    def createPrimary(self, connection:object, cursor:object, tableName:str, primaryColumn:str, columnDict:dict): 
        command = f'ALTER TABLE {tableName} MODIFY COLUMN {primaryColumn} {columnDict.get(primaryColumn)} PRIMARY KEY ({primaryColumn});'
        cursor.execute(command)
        connection.commit()

    def insertRecord(self, connection:object, cursor:object, tableName:str, columnNameList:list, values:list): 
        command = f'INSERT INTO {tableName} ({columnNameList}) VALUES ({values});'
        cursor.execute(command)
        connection.commit()

    def johnnyDropTables(self, connection:object, cursor:object, tableName):
        command = f'DROP TABLE {tableName};'
        cursor.execute(command)
        connection.commit()
    
    def removeRecord(self, connection:object, cursor:object, tableName:str, condition:str):
        command = f'DELETE FROM {tableName} WHERE {condition};'
        cursor.execute(command)
        connection.commit()

    def updateValues(self, connection:object, cursor:object, tableName:str, changeColumns:list, valuesList:list, condition:str):
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

        # self.connection.execute(createDBTable)
        # self.connection.execute(createPrimary)