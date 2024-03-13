#Jerry Dartez
#CIS 129 Lab 5
#This program counts the number of bottles returned to a company and calculates the total paid out

#declare variables

total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
keep_going = 'y'
total = 0
question = 'Enter the number of bottles for a day #'
colon = ': '
prompt = 'y'

#get the number of bottles returned for 7 days

while prompt == keep_going:
    for count in range(1, 8):
        today_bottles = int(input(f'{question}{counter}{colon}'))
        counter = counter + 1
        total_bottles = total_bottles + today_bottles
        total_payout = total_bottles * .10

#print the results of the variables' calculations

    print('Number of bottles collected', total_bottles)
    print('Total paid out is: ', format(total_payout, '.1f'))

#reset values for counter, accumulator, and calculated value

    total_payout = 0
    total_bottles = 0
    counter = 1

#reiterate the prompt to decide whether to continue or not

    prompt = (input("Do you want to enter another week's worth of data?\n"'(Enter y or n):'))


