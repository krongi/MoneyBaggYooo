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
        
        print(self.columnDict)

        