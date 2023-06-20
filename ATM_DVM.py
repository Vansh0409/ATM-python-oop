import random

# importing the module
import json

# reading the data from the file
with open("Accounts.txt") as f:
    data = f.read()
# reconstructing the data as a dictionary
js = json.loads(data)

class ATM():
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def account_details(self):
        print('\t\t*****ACCOUNT DETAILS*****')
        print(f'\t\tAccount number: {self.account_number}')
        print(f'\t\tAccount holder name: {self.name}')
        print(f'\t\tAccount Balance : {self.balance}')
        print('\t\t***************************')

    def balamce(self):
        print(f'Current balance in this account is: {self.balance}')

    def withdraw(self):
        amount = input('Please enter the amount you want to withdraw: ')
        if int(amount) > int(self.balance):
            print('You donot have enough balance in the account.')
            print(f'Your current balance is {self.balance}')
            print(f'You can withdraw upto {self.balance}')
            print('*****THANKS FOR CHOOSING THIS ATM*****')
        else:
            print(f'{amount} withdrawed from account.')
            self.balance = str(int(self.balance) - int(amount))
            a_file = open("Accounts.txt", "w")
            js[accNo][p][name] = f"{self.balance}"
            json.dump(js, a_file)
            a_file.close()
            # upgrade4 = {accNo: self.balance}
            # js[accNo][p][name].update(upgrade4)
            print(f'Current balance: {self.balance}')
            print('*****THANKS FOR CHOOSING THIS ATM*****')

    def deposit(self):
        amount = input('Please enter the amount you want to deposit: ')
        self.balance = str(int(self.balance) + int(amount))
        a_file = open("Accounts.txt", "w")
        js[accNo][p][name] = f"{self.balance}"
        json.dump(js, a_file)
        a_file.close()
        # upgrade5 = {accNo: self.balance}
        # js[accNo][p][name].update(upgrade5)
        print(f'Current balance is {self.balance}')
        print('*****THANKS FOR CHOOSING THIS ATM*****')

    def transaction(self):
        print('''*****OPTIONS*****
1. Check account - Enter 1,
2. Check balance - Enter 2,
3. Withdraw money - Enter 3,
4. Deposit money - Enter 4,
5. Exit - Enter 5''')
        try:
            task = int(input(''))
        except:
            print('Error: Please enter from 1, 2, 3, 4, 5.')
        else:
            if task == 1:
                atm.account_details()
            elif task == 2:
                atm.balamce()
            elif task == 3:
                atm.withdraw()
            elif task == 4:
                atm.deposit()
            elif task == 5:
                print(f'''*****TRANSACTION RECEIPT*****
                Account holder's name - Account
                Account Number - {self.account_number}         
                Current Balance - {self.balance}

                *****THANKS FOR CHOOSING THIS ATM*****
                ''')


print('*****WELCOME*****')
while (True):
    try:
        a = input('''Have a account? 
For YES(Enter y) or NO(Enter n)''')
    except:
        print("Please enter either 'y' or 'n'.")
    else:
        if a == 'y':
            accNo = input('Please enter account number: ')
            for key, value in js.items():
                if accNo == key:
                    p = input('Enter Pin: ')
                    for keys ,values in js[accNo].items():
                        if p == keys:
                            for keyss, valuess in js[accNo][p].items():
                                name = keyss
                                balancee = valuess
                                v = input('''Do you want to do a transaction?
    Enter 'y' if you want and 'n' if not: ''')
                                if v == 'y':
                                    atm = ATM(name, accNo, balancee)
                                    atm.transaction()
                                else:
                                    print('Enter q to exit')
                                    d = input('')
                                    if d == 'q':
                                        break
                                    elif d == 'c':
                                        continue
                                    else:
                                        print('Please enter either q or c')
                        else:
                            print('!!!WRONG PIN!!!')
                            break
        elif a == 'n':
            try:
                print('''Do you want to create an account?''')
                print('For YES(Enter y) or NO(Enter n)')
                b = input('')
            except:
                print("Please enter either 'y' or 'n'.")
            else:
                if b == 'y':
                    name = input('Please enter your name: ')
                    balan = input('How much amount do you want to deposit right now: ')
                    pinn = input('Enter a strong pin for the account')
                    Aid = str(random.randint(1000, 9999)) + name[0:1].upper() + name[-1:].upper() + str(
                        random.randint(1000, 9999))
                    print(f'''     ***ACCOUNT CREATED SUCCESSFULLY***
    Account ID is - {Aid}.
    Account holders name - {name}.
    Current Balance in account - {balan}.
    *****THANKS FOR CHOOSING US*****''')
                    a_file = open("Accounts.txt", "w")
                    y = {Aid: {pinn: {name: balan}}}
                    js.update(y)
                    json.dump(js, a_file)
                    a_file.close()

                    x = input('''\t\t\t*****THANKS*****
Enter 'c' to continue  OR  'q' to exit.''')
                    if x == 'c':
                        continue
                    elif x == 'q':
                        break
                elif b == 'n':
                    y = input('''Enter 'c' to continue  OR  'q' to exit.
            *****THANKS*****''')
                    if y == 'c':
                        continue
                    elif y == 'q':
                        break
