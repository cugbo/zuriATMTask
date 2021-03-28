#Imported datetime module to enable the user see date and time after logging in.
import datetime
currentDateTime = datetime.datetime.now()

# This is the will show the names of allowed users
name = input('What is your name? \n')
userList = ['Chima', 'Ugbo', 'Onwuka', 'Chinedu', 'Glory', 'Stanley']

# This is the password of allowed users
userPassword = ['chiPass', 'ugboPass', 'onwuPass', 'neduPass', 'gloPass', 'stanPass']

#These will show options allowed for the users
withdrawal = 1
cashDeposit = 2
customerCare = 3
# Prompting the user to input name and password
if (name in userList):
    password = input('Enter Password \n')
    userPin = userList.index(name)
# Shows a list of options available to users if password is correct    
    if (password == userPassword[userPin]):
        print(f'Welcome {name}!')
        print(currentDateTime)
        print('These are the options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaints')
# Feedback to receive if an option is selected 
        selectedOpt = int(input('Please select an option \n'))
# For Option 1
        if (selectedOpt == 1):
            print('You selected Withdral -- %s' %selectedOpt)
            print('How much would you like to withdraw?')
            amountWithdrawn = int(input('Enter Amount \n'))
            if amountWithdrawn > 0:
                print('Successful \n Please Take Your Cash')
            else:
                print('Incorrect Input, try again')
            pass
# For Option 2
        elif (selectedOpt == 2):
            print(f'You selected Cash Deposit -- {cashDeposit}')
            print('How much would you like to deposit')
            deposit = int(input('Enter Amount \n'))
            if deposit > 0:
                print('Successful')
                print(f'Current Balance is # {deposit}')
            else:
                print('Error  \n Reduce deposit')
            pass
# For Option 3
        elif (selectedOpt == 3):
            print('You selected Complaints')
            print('What issue would you like to report?')
            complaint = input('Enter Complaint \n')
            print('Thank you for contacting us')
    else:
        print('Incorrect Password \n Please Retry')
else:
    print('Name not found')
