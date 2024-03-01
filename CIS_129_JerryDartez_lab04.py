#Module 4 Lab-4
#Jerry Dartez
#2/20/24
#This programs receives input from the user as to how much in monthly sales was made and what % increase in sales was made
#It then displays store and individual bonus amounts in dollars depending on how much monthly sales were and how much % increase the sales reflected

#declare local variables
#this code gets the monthly sales and the store bonus amount
prompt = 'Enter the monthly sales:'
monthlySales = float(input(prompt))
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >=100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else: storeAmount = 0

#this section gets the increase in % of monthly sales
salesIncrease = float(input('By what percentage did monthly sales increase?'))
salesIncrease = salesIncrease / 100

#this section will calculate the individual employee bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0
    
#this section displays the results for the Store bonus and the Individual bonus
print('The store bonus amount is', '$', storeAmount)
print('The employee bonus amount is', '$', empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats!  You have reached the highest bonus amounts possible! ')

