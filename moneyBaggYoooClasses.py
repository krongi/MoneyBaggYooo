# import os
import tkinter
import customtkinter
from PIL import Image
import moneyBaggYoooDB as mdb
import dbFunctions as dbf
# import moneyBaggYooo

#Functions

def updateVars(*args):
    cashDict = getDict("cash")
    mainDict = getDict("list")
    productDict = getDict("products")
    print("Vars Updated")

def printItem(item, *args):
    print(item)

def getDict(filename):
    thisDict = {}
    f = open(filename, 'r')
    for i in f:
        [key, valueWithJunk] = i.split(": ")
        [value, junk] = valueWithJunk.split(",")
        thisDict.update({key: value})
    f.seek(0)
    f.close()
    return thisDict

def saveDict(someDict, filename):
    f = open(filename, 'w+')
    f.seek(0)
    for k in someDict:
        v = someDict.get(k)
        updateEntry = k + ": " + v + ",\n"
        f.write(updateEntry)
    f.seek(0)
    f.close
    return someDict

def readFile(filename):
    f = open(filename, 'r')
    f.seek(0)
    data = f.read()
    f.close()
    return data

def saveFile(filename, newData):
    f=open(filename, 'w')
    f.seek(0)
    f.write(str(newData))
    f.close()

def nameFromDict(someDict: dict):
    nameList = someDict.keys()
    returnedNameList = []
    for i in nameList:
        returnedNameList.append(i)
    return returnedNameList

def productMath(someDict):
    t = 0
    prodDict = getDict(someDict)
    for k in prodDict:
        v = prodDict.get(k)
        if k == 'Green Certificate':
            v = int(v)*11.5
            v = str(v)
        elif k == 'Premium License':
            v = int(v)*100
            v = str(v)
        elif k == 'Modified License':
            v = int(v)*80
            v = str(v)
        elif k == 'Hardened License':
            v = int(v)*100
            v = str(v)
        else:
            print("ERROR")
        v = float(v)
        v = round(v)
        t = t + v
    return str(t)

def dialogUserInput(title, text):
    info = GrudInputDialog(title, text)
    data = info.get_input()
    if data.isnumeric():
        return int(data)
    else:
        info.destroy()

def dialogPurchaseItem(title, text):
    info = GrudInputDialog(title, text)
    data = info.get_input()
    if data.isnumeric():
        return int(data)
    else:
        info.destroy()

def dialogGetName(title, text):
    info = GrudInputDialog(title, text)
    data = info.get_input()
    return data

# cashDict = getDict("cash")
# mainDict = getDict("list")
# productDict = getDict("products")

#Classes

class GrudCtk(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Moneybagg Yo")
        self.image = customtkinter.CTkImage(light_image=Image.open("fold.ico"), dark_image=Image.open("fold.ico"), size=(40,40))
        self.after(500, lambda :self.iconbitmap("fold.ico"))

class GrudBase(customtkinter.CTkBaseClass):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class GrudButton(customtkinter.CTkButton):
    def __init__(self, master, text="Grud Button", command=None, **kwargs):
        super().__init__(master, text=text, width=80, font=("Comic Sans", 14), command=command, **kwargs)  

class GrudScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, scrollbar_button_color="cyan", label_text="Grud Scroll Frame", label_font=("Comic Sans", 14), **kwargs)
        
class GrudFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class GrudLabel(customtkinter.CTkLabel):
    def __init__(self, master, text='', **kwargs):
        super().__init__(master, text=text, font=("Comic Sans", 14), **kwargs)
        
class GrudTextBox(customtkinter.CTkTextbox):
    def __init__(self, master):
        super().__init__(master, border_spacing=10, scrollbar_button_color="cyan", text_color="red")

class GrudEntry(customtkinter.CTkEntry):
    def __init__(self, master, placeholder_text="Grud Text Entry", **kwargs):
        super().__init__(master, placeholder_text=placeholder_text, font=("Comic Sans", 14), **kwargs)

class GrudInputDialog(customtkinter.CTkInputDialog):
    def __init__(self, title, text, **kwargs):
        super().__init__(title=title, text=text, **kwargs)
        self.after(500, lambda :self.iconbitmap("fold.ico"))

class GrudRadioButton(customtkinter.CTkRadioButton):
    def __init__(self, master, text="Grud Radio Button", command=None, **kwargs):
        super().__init__(master, text=text, font=("Comic Sans", 14), command=command)

class GrudSegmentedButton(customtkinter.CTkSegmentedButton):
    def __init__(self, master, values=None, command=None, **kwargs):
        super().__init__(master, values=values, command=command)

class GrudComboBox(customtkinter.CTkComboBox):
    def __init__(self, master, nameList, command=None, variable=None, **kwargs):
        super().__init__(master, values=nameList, command=command, variable=variable, **kwargs)

# More Complex Classes

class GrudMainWindow(GrudCtk):
    def __init__(self):
        super().__init__()

        def repayReleased(event, *args):
            print(str(self) + "\n", str(event) + "\n")
            self.infoFrame.repay(event)

        def addReleased(event, *args):
            print(event)
            self.infoFrame.add(event)

        def creditReleased(event, *args):
            if self.infoFrame.creditButton._state == "enabled":
                print(event)
                self.infoFrame.credit(event)
            else: 
                print("Button Disabled")

        self.title("Moneybagg Yo")
        self.image = customtkinter.CTkImage(light_image=Image.open("fold.ico"), dark_image=Image.open("fold.ico"), size=(40,40))
        self.after(500, lambda :self.iconbitmap("fold.ico"))
        
        self.topPane = GrudFrame(self)
        self.bottomPane = GrudFrame(self)

        self.infoFrame = GrudInfoPane(self.topPane)
        self.productsFrame = GrudProductsFrame(self.topPane)
        self.cashTotalsFrame = GrudLiquidAssetTracking(self.bottomPane)
        
        self.topPane.pack(side="top", pady=2, expand=True, fill="both")
        self.bottomPane.pack(side="bottom", padx=2, pady=5, expand=True, fill="both")

        self.infoFrame.repayButton.bind("<<RepayReleased>>", repayReleased)
        self.infoFrame.addButton.bind("<<AddReleased>>", addReleased)
        self.infoFrame.creditButton.bind("<<CreditReleased>>", creditReleased)
        self.productsFrame.increaseProductButton.bind("<<IncreaseReleased>>", self.productsFrame.increaseProduct)
        self.productsFrame.decreaseProductButton.bind("<<DecreaseReleased>>", self.productsFrame.decreaseProduct)
        self.cashTotalsFrame.cashUp.bind("<<CashUpReleased>>", self.cashTotalsFrame.addCash)
        self.cashTotalsFrame.cashDown.bind("<<CashDownReleased>>", self.cashTotalsFrame.removeCash)

        self.infoFrame.pack(side="left", padx=4, pady=2, expand=True, ipadx=6, ipady=6, fill="both")
        self.productsFrame.pack(side="right", padx=4, pady=2, expand=True, ipadx=6, ipady=6, fill="both")
        self.cashTotalsFrame.pack(side="bottom", padx=2, pady=2, expand=True, fill="both")

class GrudInfoPane(GrudFrame):
    def __init__(self, master, cursor, connection, **kwargs):
        super().__init__(master, **kwargs)
        
        # self.nameList = nameFromDict(mainDict)
        self.connection = connection
        self.cursor = cursor

        [namesList, nameBalances] = self.seedList()        
        
        

        self.event_add("<<RepayReleased>>", "<ButtonRelease-1>")
        self.event_add("<<CreditReleased>>", "<ButtonRelease-1>")
        self.event_add("<<AddReleased>>", "<ButtonRelease-1>")

        # Creating instances of classes and packing them
        self.comboBoxFrame = GrudFrame(self)
        self.buttonFrame = GrudFrame(self)
        self.label = GrudLabel(self, "Client Info")
        self.nameSelector = GrudComboBox(self.comboBoxFrame, namesList, command=self.getOwed)
        self.nameSelector.set('')
        self.selectionInfo = GrudLabel(self.comboBoxFrame, '')
        self.textboxEntry = GrudEntry(self.comboBoxFrame, 'Enter Amount')
        self.buttonFrame = GrudFrame(self)
        self.creditButton = GrudButton(self.buttonFrame, "Credit", command=self.credit)
        self.repayButton = GrudButton(self.buttonFrame, "Repay", command=self.repay)
        self.addButton = GrudButton(self.buttonFrame, "Add", command=self.add)

        # Packing instances into widget
        self.label.pack(side="top", pady=6)
        self.comboBoxFrame.pack(pady=3, ipadx=2, ipady=2)
        self.buttonFrame.pack(side="bottom", padx=6, pady=2, ipady=2, ipadx=2)
        self.nameSelector.pack(side="top", pady=2)
        self.selectionInfo.pack(side="bottom", pady=2)
        self.textboxEntry.pack(side="bottom")

        self.addButton.pack(side="left", padx=2)
        self.creditButton.pack(side="left", padx=2)
        self.repayButton.pack(side="left", padx=2)
        self.textboxEntry.configure(state="disabled")
        self.creditButton.configure(state="disabled")
        self.repayButton.configure(state="disabled")

    def seedList(self, *args):
        command = f'SELECT ClientFirst, ClientBalance FROM clients'
        self.cursor.execute(command)
        clients = self.cursor.fetchall()
        namesBalance = []
        names = []
        for i in clients:
            names.append(i[0])
            namesBalance.append([i[0], i[1]])
        return [names, namesBalance]

    def clearSelectionInfo(self, *args):
        entry = self.textboxEntry.get()
        digitCount = 0
        for i in entry:
            digitCount += 1
        self.textboxEntry.delete(0, digitCount)
        self.label.configure(True, text="Enter Amount")
        self.label.focus_set()
        self.nameSelector.set('')
        self.selectionInfo.configure(require_redraw=True, text='')
        self.textboxEntry.configure(require_redraw=True, placeholder_text = 'Enter Amount')
        self.textboxEntry.configure(state="disabled")
        self.creditButton.configure(state="disabled")
        self.repayButton.configure(state="disabled")
        
    def getOwed(self, *args):
        clientFirst = self.nameSelector.get()
        if clientFirst != '':
            command = f'SELECT ClientBalance FROM clients WHERE ClientFirst=\'{clientFirst}\''
            self.cursor.execute(command)
            amount = self.cursor.fetchone()
            amount = amount[0]
            self.connection.commit()
            # amount = mainDict.get(selection)
            self.selectionInfo.configure(True, text=clientFirst + " - $" + str(amount))
            self.repayButton.configure(state="enable")
            self.creditButton.configure(state="enable")
            self.textboxEntry.configure(state="normal")
        else:
            pass
        
    def credit(self, *args):
        nameSelected = self.nameSelector.get()
        creditApplied = self.textboxEntry.get()
        command = f'SELECT ClientID FROM clients WHERE ClientFirst=\'{nameSelected}\''
        self.cursor.execute(command)
        clientID = self.cursor.fetchone()
        clientID = clientID[0]
        try: 
            int(creditApplied)
            isInt=True
        except(TypeError, ValueError):
            print("That's not a number")
            isInt=False
        if isInt == True:
            if creditApplied != '':
                creditApplied = int(creditApplied)
                dbf.addToBalance(self.connection, self.cursor, 'clients', clientID, int(creditApplied))
                self.getOwed(nameSelected)
                self.clearSelectionInfo()
            else: 
                self.clearSelectionInfo()
                print("Nothing Done for Credit")
        else:
            print("Nothing Done to Credit")
            self.clearSelectionInfo()

    def add(self, *args):
        clientFirst = dialogGetName("Add First Name", "Enter client first name.")
        clientLast = dialogGetName("Add Last Name", "Enter client last name.")
        clientAmount = dialogUserInput("Product Value", "Total money loaned")
        try:
            int(clientAmount)
            isInt=True
        except(TypeError, ValueError):
            print("Thats not a number")
            isInt=False
        if isInt == True:
            if clientAmount != None:
                dbf.addFront(self.connection, self.cursor, [clientFirst, clientLast, int(clientAmount)])
                self.nameSelector.set('')
                self.clearSelectionInfo()
                [names, namesBalance] = self.seedList()
                self.nameSelector.configure(require_redraw=True, values=names)
                self.getOwed()
            else:
                print("Nothing Done for Add")
                self.clearSelectionInfo()
                self.seedList()
        else:
            print("Nothing Added")
            self.clearSelectionInfo()
            self.seedlist()

    def repay(self, *args):
        nameSelected = self.nameSelector.get()
        command = f'SELECT ClientBalance FROM clients WHERE ClientFirst=\'{nameSelected}\''
        self.cursor.execute(command)
        currentAmount = self.cursor.fetchone()
        currentAmount = currentAmount[0]
        repayBalance = self.textboxEntry.get()
        command = f'SELECT ClientID FROM clients WHERE ClientFirst=\'{nameSelected}\''
        self.cursor.execute(command)
        clientID = self.cursor.fetchone()
        clientID = clientID[0]
        try: 
            int(repayBalance)
            isInt=True
        except(TypeError, ValueError):
            print("That's not a number")
            isInt=False
        if isInt == True:
            if repayBalance != '':
                if int(repayBalance) == int(currentAmount):
                    dbf.makePayment(self.connection, self.cursor, 'clients', clientID, repayAmount=int(repayBalance))
                    self.getOwed(nameSelected)
                    self.clearSelectionInfo()
                    self.nameSelector.set('')
                elif int(currentAmount) > int(repayBalance):
                    dbf.makePayment(self.connection, self.cursor, 'clients', clientID, repayAmount=int(repayBalance))
                    self.getOwed(nameSelected)
                    self.clearSelectionInfo()
                    self.nameSelector.set('')
                else:
                    print("Nope, try again")
            else:
                print("Nothing Done for Repay")
        else:
            self.clearSelectionInfo()
            print("No Repayment Made")

class GrudProductsFrame(GrudFrame):
    # Shows products frame on right of the main windo
    def __init__(self, master, cursor, connection):
        super().__init__(master)

        # prodNames = nameFromDict(productDict)
        self.cursor = cursor
        self.connection = connection
        command = f'SELECT ProductName, ProductTotalAmount FROM products'
        cursor.execute(command)
        clients = cursor.fetchall()
        namesTotals = []
        names = []
        for i in clients:
            names.append(i[0])
            namesTotals.append([i[0], i[1]]) 
        self.prodNames = names
        self.prodNamesTotals = namesTotals

        self.label = GrudLabel(self, "Product Info")

        self.event_add("<<IncreaseReleased>>", "<ButtonRelease-1>")
        self.event_add("<<DecreaseReleased>>", "<ButtonRelease-1>")
        self.event_add("<<FunTimesReleased>>", "<ButtonRelease-1>")
        
        self.comboBoxFrame = GrudFrame(self)
        self.prodComboBox = GrudComboBox(self.comboBoxFrame, names, command=self.getTotals)
        self.prodComboBox.set('')
        self.totalLabel = GrudLabel(self.comboBoxFrame, '')
        self.buttonFrame = GrudFrame(self)
        self.textboxEntry = GrudEntry(self.comboBoxFrame, 'Enter Amount')
        self.increaseProductButton = GrudButton(self.buttonFrame, "Increase", command=self.increaseProduct)
        self.decreaseProductButton = GrudButton(self.buttonFrame, "Decrease", command=self.decreaseProduct)
        self.funTimesButton = GrudButton(self.buttonFrame, "Fun Times", command=None)

        self.label.pack(side="top", pady=6)
        self.comboBoxFrame.pack(pady=3, ipadx=2, ipady=2)
        self.buttonFrame.pack(pady=2, side="bottom")
        self.prodComboBox.pack(side="top", pady=2)
        self.totalLabel.pack(side="bottom", pady=2)
        self.textboxEntry.pack(side="bottom")
        
        self.increaseProductButton.pack(padx=2, side="left")
        self.decreaseProductButton.pack(padx=2, side="left")
        self.funTimesButton.pack(padx=2, side="left")
        self.textboxEntry.configure(True, state="disabled")
        self.increaseProductButton.configure(True, state="disabled")
        self.decreaseProductButton.configure(True, state="disabled")
    
    def clearTextBoxEntry(self):
        entry = self.textboxEntry.get()
        digitCount = 0
        for i in entry:
            digitCount += 1
        self.textboxEntry.delete(0, digitCount)
        self.totalLabel.focus_set()
        self.textboxEntry.configure(True, placeholder_text="Enter Amount")
        self.prodComboBox.set('')
        self.totalLabel.configure(True, text='')
        self.textboxEntry.configure(state="disabled")
        self.increaseProductButton.configure(True, state="disabled")
        self.decreaseProductButton.configure(True, state="disabled")
        
        
    def getTotals(self, selection, cursor, connection):
        # self.totalLabel.destroy()
        command = f'SELECT ProductTotalAmount FROM products WHERE ProductName={selection}'
        cursor.execute(command)
        product = self.cursor.fetchone()
        product = str(product[0]) 
        # self.totalLabel.configure(True, text=selection + ": " + str(amount) + " units")
        # self.totalLabel = GrudLabel(self, selection + ": " + str(amount) + " units")
        # self.totalLabel.pack(pady=2, side="bottom")
        self.textboxEntry.configure(True, state="normal")
        self.increaseProductButton.configure(True, state="enabled")
        self.decreaseProductButton.configure(True, state="enabled")

        
    def increaseProduct(self, *args):
        productSelected = self.prodComboBox.get()
        increase = self.textboxEntry.get()
        try: 
            int(increase)
            isInt=True
        except(TypeError, ValueError):
            print("That's not a number")
            isInt=False
        if isInt == True:
            if increase != '':
                # increase = dialogUserInput("Product Increase", "How much to increase?")
                currentAmount =  int(productDict.get(productSelected))
                newTotal = currentAmount + int(increase)
                # newTotal = str(newTotal)
                productDict.update({productSelected: str(newTotal)})
                saveDict(productDict, "products")
                self.getTotals(productSelected)
                self.clearTextBoxEntry()
        else:    
            print("Nothing Increased")
            self.clearTextBoxEntry()        
        

    def decreaseProduct(self, *args):
        productSelected = self.prodComboBox.get()
        decrease = self.textboxEntry.get()
        try: 
            int(decrease)
            isInt=True
        except(TypeError, ValueError):
            print("That's not a number")
            isInt=False
        if isInt == True:
            if decrease != '':
                currentAmount = productDict.get(productSelected)
                if currentAmount == decrease:
                    newTotal = int(currentAmount) - int(decrease)
                    productDict.update({productSelected: str(newTotal)})
                    saveDict(productDict, "products") 
                    # self.prodComboBox.configure(True, )
                    # self.prodComboBox.set('')
                    # self.totalLabel.configure(True, text='')
                    self.clearTextBoxEntry()
                elif int(currentAmount) > int(decrease):
                    newTotal = int(currentAmount) - int(decrease)
                    productDict.update({productSelected: str(newTotal)})
                    saveDict(productDict, "products")
                    self.getTotals(productSelected) 
                    self.clearTextBoxEntry()
                    
                # decrease = dialogUserInput("Product Decrease", "How much to decrease?")
                # newTotal = str(newTotal)
                # productDict.update({productSelected: str(newTotal)})
                # saveDict(productDict, "products") 
                else:    
                    # decrease = dialogUserInput("Product Decrease", "How much to decrease?")
                    # decrease = self.textboxEntry.get()
                    # currentAmount =  int(productDict.get(productSelected))
                    # newTotal = currentAmount - int(decrease)
                    # # newTotal = str(newTotal)
                    # productDict.update({productSelected: str(newTotal)})
                    # saveDict(productDict, "products")        
                    # self.getTotals(productSelected)
                    print("Nothing Decreased")
        else:
            print("Nothing Done")
        self.clearTextBoxEntry()
           
class GrudLiquidAssetTracking(GrudFrame):
    def __init__(self, master, cursor, connection, **kwargs):
        super().__init__(master, **kwargs)

        self.event_add("<<CashUpReleased>>", "<ButtonRelease-1>")
        self.event_add("<<CashDownReleased>>", "<ButtonRelease-1>")

        self.label = GrudLabel(self, "Finances")
        self.cashFrame = GrudFrame(self)
        # if cashDict.get("cash") != None:
        #     self.cashFrameLabel = GrudLabel(self.cashFrame, "Total Cash on Hand: \n$" + str(cashDict.get("cash")))
        # else:
        #     self.cashFrameLabel = GrudLabel(self.cashFrame, "You have no Cash on Hand")
        self.cashFrameButtons = GrudFrame(self.cashFrame)
        self.cashUp = GrudButton(self.cashFrameButtons, "Cash Up", command=self.addCash)
        self.cashDown = GrudButton(self.cashFrameButtons, "Cash Down", command=self.removeCash)
        self.zeroOutCashButton = GrudButton(self.cashFrameButtons, "Zero Cash", command=self.zeroOutCash)
        self.textboxEntry = GrudEntry(self.cashFrame, placeholder_text="Enter Amount")
        self.label.pack(side="top", pady=4, ipady=1)
        self.cashFrame.pack(ipady=3)
        # self.cashFrameLabel.pack(pady=3, ipady=3)
        self.cashFrameButtons.pack(side="bottom", pady=6, ipadx=4, ipady=4)
        self.cashUp.pack(padx=2, side="left")
        self.cashDown.pack(padx=2, side="right")
        self.zeroOutCashButton.pack(side="bottom")
        self.textboxEntry.pack(side="bottom")

    def clearTextEntryBox(self):
        entry = self.textboxEntry.get()
        digitCount = 0
        for i in entry:
            digitCount += 1
        self.textboxEntry.delete(0, digitCount)
        self.label.focus_set()
        self.textboxEntry.configure(True, placeholder_text="Enter Amount")
    
    def addCash(self, *args):
        amount = self.textboxEntry.get()
        try:
            int(amount)
            isInt=True
        except(TypeError, ValueError):
            print("That's not a number")
            isInt=False
        if isInt == True:
            addCash = int(amount) + int(cashDict.get("cash"))
            cashDict.update({"cash": str(addCash)})
            saveDict(cashDict, "cash")
            self.changeCashAmount()
            self.clearTextEntryBox()
        else:
            print("Nothing Added, Not a Valid Entry")
            self.clearTextEntryBox()

        # cashToAdd = dialogUserInput("Add Cash", "How much are you adding?")
        # newCash = int(cashToAdd) + int(cash)
        # saveFile("cash", newCash)
        # self.changeCashAmount(event)

    def removeCash(self, *args):
        # pass
        amount = self.textboxEntry.get()
        try:
            int(amount)
            isInt=True
        except(TypeError, ValueError):
            print("That's not a number")
            isInt=False
        if isInt == True:
            if int(cashDict.get("cash")) >= int(amount):
                removeCash =  int(cashDict.get("cash")) - int(amount)
                cashDict.update({"cash": str(removeCash)})
                saveDict(cashDict, "cash")
                self.changeCashAmount()
                self.clearTextEntryBox()
            else:
                print("Nothing Removed, Amount too Large")
                self.clearTextEntryBox()
        else:
            print("Nothing Removed, Not a Valid Entry")
            self.clearTextEntryBox()
        # cashToRemove = dialogUserInput("Remove Cash", "How much are you removing")
        # newCash = int(cash) - int(cashToRemove) 
        # saveFile("cash", newCash)
        # self.changeCashAmount(event)


    def changeCashAmount(self, *args):
        self.cashFrameLabel.configure(require_redraw=True, text="Total Cash on Hand: \n$" + str(cashDict.get("cash")))
    
    def zeroOutCash(self, *args):
        saveDict(cashDict, "cashBackup")
        cashDict.update({"cash": "0"})
        saveDict(cashDict, "cash")
        self.cashFrameLabel.configure(True, text="Total Cash on Hand: \n$" + str(cashDict.get("cash")))
        self.clearTextEntryBox()