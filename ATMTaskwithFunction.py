database = {}

import random

def generate_account_number():
    return random.randrange(1111111111, 9999999999)



def login():
    user_account_number = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for account_number,userDetails in database.items():
        if (account_number == user_account_number):
            if (userDetails[2] == password):
                bank_operations()
            else:
                print('Incorrect Password')
        else:
            print('invalid account number')



def register():
    print('*** Registration ***')
    email = input('What is your email address\n')
    first_name = input('Enter first name \n')
    last_name = input('Enter last name\n')
    middle_name = input('Enter other names\n')
    gender = int(input('Gender \n 1- Male \n 2- Female \n '))
    phone_number = int(input('Enter your phone number? \n'))
    password = input('Enter password \n')
    account_number = generate_account_number()
    database[account_number] = [first_name, email, password, account_number, phone_number, last_name, middle_name]
    print('Your account has been created')
    print('================')
    print(f'Hello {first_name} {last_name} \n Your account number is {account_number}')
    print(f'Please, keep it safe')
    print("THANKS FOR CHOOSING US \n <==Chima's bank ==> \n You can now log into your account")
    login()


def bank_operations():
    own_bank_users_acnt_num = [139800, 139801, 139802]
    own_bank_users_acnt_name = ['Okafor Ebuka', 'Odo John', 'Ugbo Chima']

    bankA_users_acnt_num = [666666, 666655]
    bankA_users_acnt_name = ['Adam Smith', 'John Keynes']

    bankB_users_acnt_num = [555554, 555555]
    bankB_users_acnt_name = ['Wisdom Eco', 'Rose Ada']

    print('How can we help you?')
    print('1- Withdrawal \n 2- Cash Deposit \n 3- Transfer \n 4- Contact Customer Care')
    option_selected_by_user = int(input('Select one option \n'))
    if (option_selected_by_user) == 1:
        print('====Withdrawal====')
        withdrawal_choice = input(
            'INSTANT WITHDRAWAL OPTION \n a- 1000 \n b- 3000 \n c- 5000 \n d- 10000 \n e- Enter Amount of Choice \n')
        if withdrawal_choice == 'a':
            print('Amount withdrawn \n #1,000')
            more_action = input('Do you want to perform another transaction \n a- yes \n b- no \n')
            if more_action == 'a':
                bank_operations()
            else:
                exit
        elif withdrawal_choice == 'b':
            print('Amount withdrawn \n #3,000')
            more_action = input('Do you want to perform another transaction \n a- yes \n b- no \n')
            if more_action == 'a':
                bank_operations()
            else:
                exit
        elif withdrawal_choice == 'c':
            print('Amount withdrawn \n #5,000')
            more_action = input('Do you want to perform another transaction \n a- yes \n b- no \n')
            if more_action == 'a':
                bank_operations()
            else:
                exit
        elif withdrawal_choice == 'd':
            print('Amount withdrawn \n #10,000')
            more_action = input('Do you want to perform another transaction \n a- yes \n b- no \n')
            if more_action == 'a':
                bank_operations()
            else:
                exit
        elif withdrawal_choice == 'e':
            print('Withdraw amount in units of #500')
            amount_entered = int(input('Enter Amount \n'))
            availableBalance = amount_entered % 500
            if availableBalance == 0:
                print('Please Take Your Cash')
                print(f'Total Withdrwal is # {amount_entered}')
                more_action = input('Do you want to perform another transaction \n a- yes \n b- no \n')
                if more_action == 'a':
                    bank_operations()
                else:
                    exit
            else:
                print('Wrong, input. \n Please retry')
        else:
            print('Wrong input')
    elif (option_selected_by_user == 2):
        print('====Cash Deposit====')
        deposit_acnt = int(input('Enter Account Number \n'))
        if deposit_acnt in own_bank_users_acnt_num:
            correct_user = own_bank_users_acnt_num.index(deposit_acnt)
            deposit_validation = input(
                f'You are depositing into {own_bank_users_acnt_name[correct_user]} account. \n a- proceed \n b- wrong account \n')
            if deposit_validation == 'a':
                amount_in = int(input('Enter amount \n'))
                print(f' SUCCESSFUL \n You have credited {own_bank_users_acnt_name[correct_user]} with #{amount_in}')
                more_action = input('Do you want to perform another transaction \n a- yes \n b- no \n')
                if more_action == 'a':
                    bank_operations()
                else:
                    exit
            elif answer == 'b':
                print('Please enter correct account')
            else:
                print('Invalid input')
        else:
            print('Invalid account number, please retry')
    elif (option_selected_by_user == 3):
        print('====Transfer====')
        bank_of_choice = input('a- Transfer to own bank \n b- Transfer to other banks \n')
        if bank_of_choice == 'a':
            own_acnt_num = int(input("Enter the Chima's Bank account number \n"))
            if own_acnt_num in own_bank_users_acnt_num:
                valid_user = own_bank_users_acnt_num.index(own_acnt_num)
                transfer_validation = input(
                    f'You are transfering into {own_bank_users_acnt_name[valid_user]} account. \n a- proceed \n b- wrong account \n')
                if transfer_validation == 'a':
                    amount_trans = int(input('Enter amount \n'))
                    print(
                        f' SUCCESSFUL \n You have transfered #{amount_trans} to {own_bank_users_acnt_name[valid_user]}')
                    more_action = input('Do you want to perform another transaction \n a- yes \n b- no \n')
                    if more_action == 'a':
                        bank_operations()
                    else:
                        exit
                elif transfer_validation == 'b':
                    print('Re-enter account number')
                else:
                    print('Invalid input')

            else:
                print('Invalid account number')
        elif bank_of_choice == 'b':
            other_bank_options = input('a- Bank A \n b- Bank B \n')
            if other_bank_options == 'a':
                bank_a_acnt_no = int(input('Enter Bank A account number \n'))
                if bank_a_acnt_no in bankA_users_acnt_num:
                    valid_bank_a = bankA_users_acnt_num.index(bank_a_acnt_no)
                    bank_a_validation = input(
                        f'You are transfering into {bankA_users_acnt_name[valid_bank_a]} account. \n a- proceed \n b- wrong account \n')
                    if bank_a_validation == 'a':
                        bank_a_trans_amount = int(input('Enter amount \n'))
                        print(
                            f' SUCCESSFUL \n You have transfered #{bank_a_trans_amount} to {bankA_users_acnt_name[valid_bank_a]}')
                        more_action = input('Do you want to perform another transaction \n a- yes \n b- no \n')
                        if more_action == 'a':
                            bank_operations()
                        else:
                            exit


                    elif bank_a_validation == 'b':
                        print('Please reconfirm account number')
                    else:
                        print('Invalid input')

                else:
                    print('Enter a valid account number')

            elif other_bank_options == 'b':
                bankBs_acnt_no = int(input('Enter Bank B account number \n'))
                if bankBs_acnt_no in bankB_users_acnt_num:
                    valid_bank_b = bankB_users_acnt_num.index(bankBs_acnt_no)
                    bank_b_validation = input(
                        f'You are transfering into {bankB_users_acnt_name[valid_bank_b]} account. \n a- proceed \n b- wrong account \n')
                    if bank_b_validation == 'a':
                        bankB_transfer_sum = int(input('Enter amount \n'))
                        print(
                            f' SUCCESSFUL \n You have transfered #{bankB_transfer_sum} to {bankB_users_acnt_name[valid_bank_b]}')
                        more_action = input('Do you want to perform another transaction \n a- yes \n b- no \n')
                        if more_action == 'a':
                            bank_operations()
                        else:
                            exit
                    elif bank_b_validation == 'b':
                        print('Please reconfirm account number')

                else:
                    print('Enter a valid account number')
        else:
            print('Invalid option')

    elif (option_selected_by_user == 4):
        print('====Contact Customer Care====')
        contact_care = input(
            'a- Frequently asked questions \n b- Send a type in your complaint \n c- Speak to a customer care representative \n')
        if contact_care == 'a':
            options = input(
                'i. How to create an account \n ii. forgot password \n iii. unsuccessful transaction but got debited \n')
            if options == 'i' or 'ii' or 'iii':
                print('Please Visit: www.bankhelpwebpage.com')
            else:
                print('Invalid option')

        elif contact_care == 'b':
            complaint_msg = input('Type in your complaint \n')
            print('We will get back to you')
            more_action = input('Do you want to perform another transaction \n a- yes \n b- no \n')
            if more_action == 'a':
                bank_operations()
            else:
                exit
        elif contact_care == 'c':
            print('Connecting to a customer care representative...')
        else:
            print('Wrong option selected')


    else:
        print('Wrong Option \n Please Retry')


def initialize():
    valid_option = False
    print("Welcome to Chima's bank")
    while valid_option == False:
        try:
            have_account = int(input('Do you have account with us: \n 1- Yes. 2- No \n'))
            if have_account == 1:
                valid_option = True
                print('You can now log in')
                own_users_account_number = [20000, 30000, 40000]
                own_users_password = [2222, 3333, 4444]
                own_users_account_number = int(input('Enter Account Number \n'))

                if ac_number in own_users_account_number:
                    ac_password = int(input('Enter Password \n'))
                    if own_users_account_number.index(ac_number) == own_users_password.index(ac_password):
                        bank_operations()
                    else:
                        print('Password incorrect')

                else:
                    print('Incorrect Account Number')


            elif have_account == 2:
                valid_option = True
                print('Please fill in your details')
                register()
            else:
                print('Invalid input')
        except Exception as e:
            print('Please, enter an integer', e)


initialize()
