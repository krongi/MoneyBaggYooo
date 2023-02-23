import customtkinter
import moneyBaggYoooClasses as mc

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def repayCashUpdate(*args):
    infoFrame.repay()
    financeFrame.changeCashAmount()
    infoFrame.clearSelectionInfo()

main = mc.GrudCtk()

infoFrame = mc.GrudInfoPane(main)
productFrame = mc.GrudProductsFrame(main)
financeFrame = mc.GrudLiquidAssetTracking(main)

mainFrames = [infoFrame, productFrame, financeFrame]

infoFrame.pack(side="left", expand=True, fill="y")
financeFrame.pack(side="left", padx=2, expand=True, fill="y")
productFrame.pack(side="left", expand=True, fill="y")

infoFrame.repayButton.configure(False, command=repayCashUpdate)

main.mainloop()