# Title:			PiggyBankv2.py
# Author:		Lennox Stampp
# Date:			1-6-22
# Purpose:	 Store piggy bank balances with
#					   the different percentages, version 2


import pickle
import tkinter as tk
import time
#from tkinter import ttk

# Piggy banks
HarmonyBank = {'bal': 0.0, 'longSavings': 0.0,'shortSavings': 0.0,  'spending': 0.0, 'donation': 0.0, 'note':[]}
FarrahBank = {'bal': 0.0, 'longSavings': 0.0,'shortSavings': 0.0,  'spending': 0.0, 'note':[], 'donation': 0.0}
NoraBank = {'bal': 0.0, 'longSavings': 0.0,'shortSavings': 0.0,  'spending': 0.0, 'note':[],'donation': 0.0}
NoxyBank = {'bal': 0.0, 'longSavings': 0.0,'shortSavings': 0.0,  'spending': 0.0, 'note':[], 'donation': 0.0}
LincolnBank = {'bal': 0.0, 'longSavings': 0.0,'shortSavings': 0.0,  'spending': 0.0, 'note':[], 'donation': 0.0}

#GUI

# Main window
window = tk.Tk()
window.config(bg="#7ec1ed")

# Space holders for alignment of screen objects

lb1 = tk.Label(window) #this ain't it!
lb1.grid(row=0, column=0) #nope
#lb1.grid_forget() #nope
tk.Label(window).grid(row=1, column=1) #leaves a line on the screen!
tk.Label(window).grid(row=4, column=0)
tk.Label(window).grid(row=5, column=1)

# Display area
dispText = tk.Text(window, height=20, width=40)
dispText.grid(row=6, columns=3)
dispText.grid_forget()

# Change text area bg color to same bg color as button
def colorIt(button, displayArea):
	getColor = button.cget('bg')
	displayArea.config(bg=getColor)

# Button Functions

# View Account details
def viewAcctDet(bank, button):
	notes = ""
	for note in bank['note']:
		notes += note
		
	name = button.cget('text')
	details = f"{name}'s piggy bank: \nTotal balance: ${bank['bal']:,.{2}f} \nMad Money: ${bank['spending']:,.{2}f} \nLong term savings: ${bank['longSavings']:,.{2}f} \nShort term savings: ${bank['shortSavings']:,.{2}f} \nDonation balance: ${bank['donation']:,.{2}f} \nAccount notes: {notes} "
	dispText.delete("1.0", tk.END)  
	dispText.insert(tk.END, details)
	dispText.grid(row=6, columns=3)
	
def updActvAcct(event, bank):
	actvAcct.clear()
	actvAcct.append(bank)
	actvAcct.append(event.widget)
	
	dispText.delete("1.0", tk.END)
	name = event.widget.cget("text")
	msg = f"{name} account loaded"
	dispText.insert(tk.END, msg)

actvAcct = []        #0-bank obj  1-widget obj


def mkDeposit(amount, bank):
	amount = float(amount)
	longSavings = float(amount) * .2
	shortSavings = float(amount) * .3	
	spending = float(amount) * .4
	donation = float(amount) * .1
	bank.update({'bal':(amount + bank['bal']),'longSavings':(longSavings + bank['longSavings']),'shortSavings':(shortSavings + bank['shortSavings']),  'spending':(spending + bank['spending']), 'donation':
		(donation + bank['donation'])})
		
def depositWin():
	
	def getDepst():
		return float(entryField.get())
		
	def submit(windw, amount):
		mkDeposit(amount, actvAcct[0])
		name = actvAcct[1].cget("text")
		msg = f"\nDeposit made for {name} in the \namount of ${amount:,.{2}f}"
		dispText.insert(tk.END, msg)
		windw.destroy()
	
	def clearEntry():
		entryField.delete(first=0, last=tk.END)
	
	newWin = tk.Tk()
	
	entryField = tk.Entry(newWin, exportselection=0)
	entryField.pack()
		
	submitBtn = tk.Button(newWin, text='Submit', command=lambda:submit(newWin, getDepst()))
	submitBtn.pack()
	
	clearBtn = tk.Button(newWin, text='Clear', command=lambda:clearEntry())
	clearBtn.pack()
	
	closeWin = tk.Button(newWin, text='Close', command=lambda:newWin.destroy())
	closeWin.pack()
	
# def mkWithdrawl(amount, bank):
	

def withdrwalWin():
	
	wWin = tk.Tk()
	
	name = actvAcct[1].cget("text")
	ltsBal = actvAcct[0]['longSavings']
	shtBal = actvAcct[0]['shortSavings']
	spdBal = actvAcct[0]['spending']
	dntBal = actvAcct[0]['donation']
	longCkVal = tk.IntVar(wWin)
	shortCkVal = tk.IntVar(wWin)
	spendCkVal = tk.IntVar(wWin)
	donatCkVal = tk.IntVar(wWin)
	
	
	def chkdBox():
		if longCkVal.get() == 1:
			longEnt.config(state = 'normal')	
		elif longCkVal.get() == 0:
			longEnt.delete(0, tk.END)
			longEnt.config(state = 'disabled')
			
		if shortCkVal.get() == 1:
			shortEnt.config(state = 'normal')	
		elif shortCkVal.get() == 0:
			shortEnt.delete(0, tk.END)
			shortEnt.config(state = 'disabled')
			
		if spendCkVal.get() == 1:
			spendEnt.config(state = 'normal')	
		elif spendCkVal.get() == 0:
			spendEnt.delete(0, tk.END)
			spendEnt.config(state = 'disabled')
			
		if donatCkVal.get() == 1:
			donatEnt.config(state = 'normal')	
		elif donatCkVal.get() == 0:
			donatEnt.delete(0, tk.END)
			donatEnt.config(state = 'disabled')
			
	def clearEnt():
		longEnt.delete(0,tk.END)
		shortEnt.delete(0,tk.END)
		spendEnt.delete(0,tk.END)
		donatEnt.delete(0,tk.END)
		
	def wthdrwlUpdt(bank):
		longSavings = 0.0
		shortSavings = 0.0
		spending = 0.0
		donation = 0.0
		sumWdrw = longSavings + shortSavings + spending + donation
		
		if longCkVal.get() == 1:
			longSavings += float(longEnt.get())
		if shortCkVal.get() == 1:
			shortSavings += float(shortEnt.get())
		if spendCkVal.get() == 1:
			spending += float(spendEnt.get())
		if donatCkVal.get() == 1:
			donation += float(donatEnt.get())
		
		bank.update({'bal':(bank['bal'] - sumWdrw),'longSavings':(bank['longSavings'] - longSavings),'shortSavings':(bank['shortSavings'] - shortSavings),  'spending':(bank['spending'] - spending), 'donation':
		(bank['donation'] - donation)})
		
	def submitWdrwl(windw, bank):
		wthdrwlUpdt(bank)
		try:
			lngAmount = float(longEnt.get()) + 0.0
		except:
			lngAmount = 0.0
		try:
			shAmount = float(shortEnt.get()) + 0.0
		except:
			shAmount = 0.0
		try:
			spdAmount = float(spendEnt.get()) + 0.0
		except:
			spdAmount = 0.0
		try:
			dntAmount = float(donatEnt.get()) + 0.0
		except:
			dntAmount = 0.0
		try:
			sumAmount = lngAmount + shAmount + spdAmount + dntAmount
		except:
			sumAmount = 0.0
		name = actvAcct[1].cget("text")
		msg = f"\nWithdrawl made for {name} in the \namount of ${sumAmount:,.{2}f}"
		dispText.insert(tk.END, msg)
		windw.destroy()
	
	labelTitle = tk.Label(wWin, text=f"Withdrawl from {name}'s account")
	labelTitle.grid(row=0, columns=4)
	longsavLbl = tk.Label(wWin, text="Long Term Savings:")
	longsavLbl.grid(row=1, column=0)
	shortsavLbl = tk.Label(wWin, text="Short Term Savings:")
	shortsavLbl.grid(row=2, column=0)
	spendingLbl = tk.Label(wWin, text="Mad Money:")
	spendingLbl.grid(row=3, column=0)
	donationLbl = tk.Label(wWin, text="Donation:")
	donationLbl.grid(row=4, column=0)
	
	longCkbx = tk.Checkbutton(wWin,variable=longCkVal, onvalue=1, offvalue=0, command=chkdBox)
	longCkbx.grid(row=1, column=1)
	#longCkbx.bind('<ButtonPress>', lambda event: chkdBox())
	shortCkbx = tk.Checkbutton(wWin, variable=shortCkVal, onvalue=1, offvalue=0, command=chkdBox)
	shortCkbx.grid(row=2, column=1)
	spendCkbx = tk.Checkbutton(wWin, variable=spendCkVal, onvalue=1, offvalue=0, command=chkdBox)
	spendCkbx.grid(row=3, column=1)
	donatCkbx = tk.Checkbutton(wWin, variable=donatCkVal, onvalue=1, offvalue=0, command=chkdBox)
	donatCkbx.grid(row=4, column=1)
	
	longEnt = tk.Entry(wWin, state='disabled')
	longEnt.grid(row=1, column=2)
	shortEnt = tk.Entry(wWin, state='disabled')
	shortEnt.grid(row=2, column=2)
	spendEnt = tk.Entry(wWin, state='disabled')
	spendEnt.grid(row=3, column=2)
	donatEnt = tk.Entry(wWin, state='disabled')
	donatEnt.grid(row=4, column=2)
	
	lBalLbl = tk.Label(wWin, text=f"${ltsBal:,.{2}f}")
	lBalLbl.grid(row=1, column=3)
	shBalLbl = tk.Label(wWin, text=f"${shtBal:,.{2}f}")
	shBalLbl.grid(row=2, column=3)
	spBalLbl = tk.Label(wWin, text=f"${spdBal:,.{2}f}")
	spBalLbl.grid(row=3, column=3)
	dBalLbl = tk.Label(wWin, text=f"${dntBal:,.{2}f}")
	dBalLbl.grid(row=4, column=3)
	
	submitBtn = tk.Button(wWin, text='Submit')
	submitBtn.grid(row=5, columns=4, pady=8)
	submitBtn.bind('<ButtonPress>', lambda windw=wWin,bank=actvAcct[0]:submitWdrwl(wWin, bank))
	clearBtn = tk.Button(wWin, text='Clear', command=clearEnt)
	clearBtn.grid(row=6, columns=4, pady=8)
	closeBtn = tk.Button(wWin, text='Close', command=lambda:wWin.destroy())
	closeBtn.grid(row=7, columns=4, pady=8)
	
def addNoteWin():
	aWin = tk.Tk()
	timeStamp = time.ctime()
	topLbl = tk.Label(aWin, text='Enter note here.\nThis is considered one entry to the Add Notes section.')
	topLbl.pack()
	
	def clearTxt():
		noteArea.delete("1.0", tk.END)
		
	def submitNote():
		note = noteArea.get("1.0", tk.END)
		actvAcct[0]['note'].append('\n  |__ ' + timeStamp + ' ---- :\n\t' + note)
		viewAcctDet(actvAcct[0], actvAcct[1])
		aWin.destroy()
	
	bgClr = actvAcct[1].cget('bg')
	noteArea = tk.Text(aWin, height=25, width=45, bg=bgClr)
	noteArea.pack()
	
	submitBtn = tk.Button(aWin, text='Submit', pady=8, command=submitNote)
	submitBtn.pack()
	clearBtn = tk.Button(aWin, text='Clear All', pady=8, command=clearTxt)
	clearBtn.pack()
	closeBtn = tk.Button(aWin, text='Close', pady=8, command=lambda:aWin.destroy())
	closeBtn.pack()


######### for testing #############

def printTxt(button):
	dispText.delete("1.0", tk.END)
	name = button.cget("text")
	dispText.insert(tk.END, f"{name} button pressed")
	dispText.insert(tk.END,f"{actvAcct[0]}, {actvAcct[1]}")
	
def mkTxtWht(event, bank):
	event.widget.config(fg="white")
	dispText.config(fg='white')
	updActvAcct(event, bank)

##############################

# Piggy bank holders
harmBtn = tk.Button(window, text="Harmony", bg='Pink', command=lambda:colorIt(harmBtn, dispText))
harmBtn.grid(row=2, column=0)
harmBtn.bind('<ButtonPress>', lambda event, bank=HarmonyBank: [updActvAcct(event, bank), viewAcctDet(actvAcct[0], actvAcct[1])])

farrBtn = tk.Button(window, text="Farrah", bg='Yellow', command=lambda:colorIt(farrBtn, dispText))
farrBtn.grid(row=2, column=1)
farrBtn.bind('<ButtonPress>', lambda event, bank=FarrahBank: [updActvAcct(event, bank), viewAcctDet(actvAcct[0], actvAcct[1])])

noraBtn = tk.Button(window, text="Nora", bg='Purple', command=lambda: colorIt(noraBtn, dispText))
noraBtn.grid(row=2, column=2)
noraBtn.bind('<ButtonPress>', lambda event, bank=NoraBank: [updActvAcct(event, bank), viewAcctDet(actvAcct[0], actvAcct[1])])

noxyBtn = tk.Button(window, text="Lennox III", bg='#3366ff', command=lambda:colorIt(noxyBtn, dispText))
noxyBtn.grid(row=3, column=0)
noxyBtn.bind('<ButtonPress>', lambda event, bank=NoxyBank: [updActvAcct(event, bank), viewAcctDet(actvAcct[0], actvAcct[1])])

lincBtn = tk.Button(window, text="Lincoln", bg='Orange', command=lambda:colorIt(lincBtn, dispText))
lincBtn.grid(row=3, column=1)
lincBtn.bind('<ButtonPress>', lambda event, bank=LincolnBank: [updActvAcct(event, bank), viewAcctDet(actvAcct[0], actvAcct[1])])

# Action buttons
vAcctBtn = tk.Button(window, text="View Account", command=lambda:viewAcctDet(actvAcct[0], actvAcct[1]))
vAcctBtn.grid(row=7, column=0)

dpstBtn = tk.Button(window, text="Deposit", command=depositWin)
dpstBtn.grid(row=7, column=1)
lincBtn.bind('<ButtonPress>', lambda event, bank=LincolnBank: [updActvAcct(event, bank), viewAcctDet(actvAcct[0], actvAcct[1])])

wdrwBtn = tk.Button(window, text="Withdrawl", command=withdrwalWin)
wdrwBtn.grid(row=8, column=0)
wdrwBtn.bind('<ButtonPress>', lambda: viewAcctDet(actvAcct[0], actvAcct[1]))

noteBtn = tk.Button(window, text="Add Note", command=addNoteWin)
noteBtn.grid(row=8, column=1)
noteBtn.bind('<ButtonPress>', lambda: viewAcctDet(actvAcct[0], actvAcct[1]))

quitBtn = tk.Button(window, text="Quit No Save", command=window.quit)
quitBtn.grid(row=9, column=0)

quitAndsaveBtn = tk.Button(window, text="Save and Quit")
quitAndsaveBtn.grid(row=9, column=1)


	   
	   
tk.mainloop()	   
window.mainloop()