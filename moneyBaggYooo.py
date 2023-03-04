import customtkinter
import moneyBaggYoooClasses as mc
import moneyBaggYoooDB as mdb
import dbFunctions as dbf

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

[connection, cursor] = mdb.connection()


def repayCashUpdate(*args):
    infoFrame.repay()
    financeFrame.changeCashAmount()
    infoFrame.clearSelectionInfo()
main = mc.GrudCtk()

infoFrame = mc.GrudInfoPane(main, cursor=cursor, connection=connection)
productFrame = mc.GrudProductsFrame(main, cursor=cursor, connection=connection)
financeFrame = mc.GrudLiquidAssetTracking(main, cursor=cursor, connection=connection)

mainFrames = [infoFrame, productFrame, financeFrame]

infoFrame.pack(side="left", expand=True, fill="y")
financeFrame.pack(side="left", padx=2, expand=True, fill="y")
productFrame.pack(side="left", expand=True, fill="y")

# infoFrame.repayButton.configure(False, command=repayCashUpdate)
# infoFrame.nameSelector.bind("<ButtonRelease-1>", infoFrame.getOwed)

main.mainloop()