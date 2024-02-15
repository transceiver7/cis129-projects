"""Module 3: Lab"""
"""Coffee Shop Simulator"""
"""Author:  Jerry Dartez"""
"""CIS_129_lab03_coffeeShop.py"""

#This section prints the opening output for the Coffee Shop Program
#Also requests input from the user as to how many items to purchase
print("************************")
print("My Coffee and Muffin Shop")
coffee = int(input("Number of Coffees bought?\n"))
muffin = int(input("Number of Muffins bought?\n"))
print("*************************\n")
print("\n*************************")

#This section prints the receipt
#Sets the variables for costs of items
#Prints number and cost of each item depending on 'if' statements
print("My Coffee and Muffin Shop Receipt")
CoffeePrice = float(5.00)
MuffinPrice  = float(4.00)

if coffee == 1:
    print(coffee, 'Coffee', 'at', '$5', 'each:', '$', coffee * CoffeePrice)
if coffee > 1:
    print(coffee, 'Coffees', 'at', '$5', 'each:', '$', coffee * CoffeePrice)
if muffin == 1:
    print(muffin, 'Muffin', 'at', '$4', 'each:', '$', muffin * MuffinPrice)
if muffin > 1:
    print(muffin, 'Muffins', 'at', '$4', 'each:', '$', muffin * MuffinPrice)

#This section calculates totals and prints final part of receipt
total = (coffee + CoffeePrice) + (muffin * MuffinPrice) 
total = float(total)
tax = (total * .06)
FinalTax = round(tax,2)
print('6% Tax:', '$', FinalTax)
TaxTotal = total * 1.06
FinalTotal = round(TaxTotal,2)
print('----------------------')
print('Total: $', FinalTotal)
print('********************************')