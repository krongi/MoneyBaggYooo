
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
    currentAmount = cursor.fetchone()
    currentAmount = currentAmount[0]
    newAmount = currentAmount + balanceAdd
    command = f'UPDATE {tableName} SET ClientBalance={newAmount} WHERE ClientID={clientID};'
    cursor.execute(command)
    connection.commit()

def makePayment(connection:object, cursor:object, tableName:str, clientID:int, repayAmount:int):
    command = f'SELECT ClientBalance FROM {tableName} WHERE ClientID={clientID}'
    cursor.execute(command)
    currentAmount = cursor.fetchone()
    currentAmount = currentAmount[0]
    newAmount = currentAmount - repayAmount
    command = f'UPDATE {tableName} SET ClientBalance={newAmount} WHERE ClientID={clientID};'
    cursor.execute(command)
    connection.commit()


#Product Table Functions
def addProducts(connection:object, cursor:object, values:list):
    command = f'INSERT INTO products (ProductName, ProductCostPerUnit, ProductPricePerUnit, ProductTotalAmount) VALUES (%s,%s,%s,%s)'
    cursor.execute(command, values)
    connection.commit()

def increaseProductTotal(connection:object, cursor:object, value:str, productName:str):
    command = f'SELECT ProductTotalAmount FROM products WHERE ProductName=\'{productName}\''
    cursor.execute(command)
    currentAmount = cursor.fetchone()
    currentAmount = currentAmount[0]
    newAmount = int(currentAmount) + int(value)
    newAmount = str(newAmount)
    command = f'UPDATE products SET ProductTotalAmount=\'{newAmount}\' WHERE ProductName=\'{productName}\''
    cursor.execute(command)
    connection.commit()

def reduceProductTotal(connection:object, cursor:object, value:str, productName:str):
    command = f'SELECT ProductTotalAmount FROM products WHERE ProductName=\'{productName}\''
    cursor.execute(command)
    currentAmount = cursor.fetchone()
    currentAmount = currentAmount[0]
    if int(currentAmount) >= int(value):
        newAmount = int(currentAmount) - int(value)
        newAmount = str(newAmount)
        command = f'UPDATE products SET ProductTotalAmount=\'{newAmount}\' WHERE ProductName=\'{productName}\''
        cursor.execute(command)
        connection.commit()
    else:
        print('Entry too high, can not be greater than\ncurrent total!')

def changeProductCost(connection:object, cursor:object, productName:str, newCost:str):
    command = f'UPDATE products SET ProductCostPerUnit=\'{newCost}\' WHERE ProductName=\'{productName}\''
    cursor.execute(command)
    connection.commit()

def changeProductPrice(connection:object, cursor:object, productName:str, newPrice:str):
    command = f'UPDATE products SET ProductPricePerUnit=\'{newPrice}\' WHERE ProductName=\'{productName}\''
    cursor.execute(command)
    connection.commit()

# Asset table functions
def addCash(connection:object, cursor:object, increase, assetName:str='Cash'):
    command = f'SELECT AssetValue FROM assets WHERE AssetName=\'{assetName}\''
    cursor.execute(command)
    currentAmount = cursor.fetchone()
    currentAmount = currentAmount[0]
    newAmount = int(currentAmount) + int(increase)
    command = f'UPDATE assets SET AssetValue=\'{newAmount}\''
    cursor.execute(command)
    connection.commit()

def reduceCash(connection:object, cursor:object, decrease, assetName:str='Cash'):
    command = f'SELECT AssetValue FROM assets WHERE AssetName=\'{assetName}\''
    cursor.execute(command)
    currentAmount = cursor.fetchone()
    currentAmount = currentAmount[0]
    newAmount = int(currentAmount) - int(decrease)
    command = f'UPDATE assets SET AssetValue=\'{newAmount}\''
    cursor.execute(command)
    connection.commit()

def getAssets(connection:object, cursor:object, assetName:str='Cash', columnName:str='AssetValue', table:str='assets'):
    command = f'SELECT {columnName} FROM {table} WHERE AssetName=\'{assetName}\''
    cursor.execute(command)
    assets = cursor.fetchone()
    assets = assets[0]
    return assets
    
def johnnyDropTables(connection:object, cursor:object, tableName):
    command = f'DROP TABLE {tableName};'
    cursor.execute(command)
    connection.commit()