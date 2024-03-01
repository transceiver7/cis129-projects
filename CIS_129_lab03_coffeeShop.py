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
scone = int(input("Number of Scones bought?\n"))
brownie = int(input("Number of Brownies bought?\n"))
print("*************************\n")
print("\n*************************")

#This section prints the receipt
#Sets the variables for costs of items
print("My Coffee and Muffin Shop Receipt")
CoffeePrice = float(5.00)
MuffinPrice  = float(4.00)
SconePrice = float(3.50)
BrowniePrice = float(2.75)

#This section totals the cost of each item using the prices from above * user input
CoffeeTotal = coffee * CoffeePrice
MuffinTotal = muffin * MuffinPrice
SconeTotal = scone * SconePrice
BrownieTotal = brownie * BrowniePrice

#In this section, I use the --- format(value, '.2f)  --- to force 2 zeros
#This secton also prints number and cost of each item depending on 'if' statements
if coffee == 1:
    print(coffee, 'Coffee', 'at', '$5', 'each:', '$', (format(CoffeeTotal, '.2f')))
if coffee > 1:
    print(coffee, 'Coffees', 'at', '$5', 'each:', '$', (format(CoffeeTotal, '.2f')))
if muffin == 1:
    print(muffin, 'Muffin', 'at', '$4', 'each:', '$', (format(MuffinTotal, '.2f')))
if muffin > 1:
    print(muffin, 'Muffins', 'at', '$4', 'each:', '$', (format(MuffinTotal, '.2f')))
if scone == 1:
    print(scone, 'Scone', 'at', '$3.50', 'each:', '$', (format(SconeTotal, '.2f')))
if scone > 1:
    print(scone, 'Scones', 'at', '$3.50', 'each:', '$', (format(SconeTotal, '.2f')))
if brownie == 1:
    print(brownie, 'Brownie', 'at', '$2.75', 'each', '$', (format(BrownieTotal, '.2f')))
if brownie > 1:
    print(brownie, 'Brownies', 'at', '$2.75', 'each', '$', (format(BrownieTotal, '.2f')))


#This section calculates totals and prints final part of receipt
total = (coffee + CoffeePrice) + (muffin * MuffinPrice) + (scone * SconePrice) + (brownie * BrowniePrice)
total = float(total)
tax = (total * .06)
FinalTax = round(tax,2)
print('6% Tax:', '$', FinalTax)
TaxTotal = total * 1.06
FinalTotal = round(TaxTotal,2)
print('----------------------')
print('Total: $', FinalTotal)
print('********************************')