# Title:			PiggyBank
# Author:		Lennox Stampp
# Date:			1-4-2022
# Purpose:	 Store piggy bank balances with
#					   the different percentages

import pickle
#import tkinter as tk

# Piggy banks
HarmonyBank = {'bal': 0.0, 'longSavings': 0.0,'shortSavings': 0.0,  'spending': 0.0, 'donation': 0.0}
FarrahBank = {'bal': 0.0, 'longSavings': 0.0,'shortSavings': 0.0,  'spending': 0.0, 'donation': 0.0}
NoraBank = {'bal': 0.0, 'longSavings': 0.0,'shortSavings': 0.0,  'spending': 0.0, 'donation': 0.0}
NoxyBank = {'bal': 0.0, 'longSavings': 0.0,'shortSavings': 0.0,  'spending': 0.0, 'donation': 0.0}
LincolnBank = {'bal': 0.0, 'longSavings': 0.0,'shortSavings': 0.0,  'spending': 0.0, 'donation': 0.0}

try:
	with open('PiggyBank.py', 'rb') as loadFile:
		HarmonyBank, FarrahBank, NoraBank, NoxyBank, LincolnBank = pickle.load(loadFile)
		print('banks accts loaded')

except:
	print('Data not loaded')
	
def balSplit(bankObj, bal):
	bal = float(bal)
	longSavings = float(bal) * .2
	shortSavings = float(bal) * .3	
	spending = float(bal) * .4
	donation = float(bal) * .1
	bank.update({'bal':(bal + bankObj['bal']), 'longSavings':(longSavings + bankObj['longSavings']),'shortSavings':(shortSavings + bankObj['shortSavings']),  'spending':(spending + bankObj['spending']), 'donation':
		(donation + bankObj['donation'])})
		
def getBank(name):
		name = name.lower()
		if name == "harmony":
			return HarmonyBank
		elif name == "farrah":
			return FarrahBank
		elif name == "nora":
			return NoraBank
		elif name == "lennox":
			return NoxyBank
		elif name == "lincoln":
			return LincolnBank
		

while True:
	piggyBank = input("Enter piggy bank owner's name:")
	depositAmnt = input("Enter the amount to be deposited into " + piggyBank + "'s piggy bank: ")
	print(f"...adding ${depositAmnt} to {piggyBank} ")
	bank = getBank(piggyBank)
	balSplit(bank, depositAmnt)
	print(f"${depositAmnt} has been deposited into bank")
	
	with open('PiggyBank.py', 'wb') as saveFile:
	   pickle.dump([HarmonyBank, FarrahBank, NoraBank, NoxyBank, LincolnBank], saveFile)
	   
	checkBal = input(f"Would you like to check the balance of {piggyBank}? (y/n): ")
	if checkBal.lower() == 'y':
	   print(f"{piggyBank}'s piggy bank: \n \
	   Total balance: ${bank['bal']:,.{2}f} \n \
	   Mad Money: ${bank['spending']:,.{2}f} \n \
	   Long term savings: ${bank['longSavings']:,.{2}f} \n \
	   Short term savings: ${bank['shortSavings']:,.{2}f} \n \
	   Donation balance: ${bank['donation']:,.{2}f}")
	   
	addMore = input("Would you like to add another deposit? (y/n): ")
	if addMore.lower() == 'n':
		break
	elif addMore.lower() == 'y':
		continue
		

#with open('PiggyBank.py', 'wb') as loadFile:
#	pickle.dump([],loadFile)
#	print(".......deleted data........")