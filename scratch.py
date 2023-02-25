import mysql.connector
class TableSetup():
    def __init__(self, connectionCursor, tableName, primaryColumn, columnNameList, columnTypeList) -> None:
        self.tableName = tableName
        self.columnNameList = columnNameList
        self.columnType = columnTypeList
        self.primaryColumn = primaryColumn
        self.connection = connectionCursor

        self.columnDict = {} 
        counter = 0

        for i in self.columnNameList:
            self.columnDict.update({str(self.columnNameList[counter]): str(columnTypeList[counter])})
            counter += 1
        
        counter = 0
        
        columnNameTypeString = ''

        for i in self.columnDict:
            if counter+1 < len(self.columnDict):
                name = i
                value = self.columnDict.get(i)
                columnNameTypeString += name + " " + value + ", "
                counter += 1
            else:
                name = i
                value = self.columnDict.get(i)
                columnNameTypeString += name + " " + value
                counter = 0
        print(columnNameTypeString)

        createDBTable = f'CREATE TABLE {self.tableName} ({columnNameTypeString});'
        # createPrimary = f'ALTER TABLE {self.tableName} MODIFY COLUMN {primaryColumn} {self.columnDict.get(primaryColumn)}'

        self.connection.execute(createDBTable)
        # self.connection.execute(createPrimary)

