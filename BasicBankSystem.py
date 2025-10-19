def deposit(balance, amount, tr_history):
    balance+= amount
    tr_history.append((balance,amount))
    print(f'Deposited {amount}. The new balance is {balance}')
    return balance

def withdraw(balance, amount,tr_history):
    if balance-amount >= 0:
        balance-=amount
        tr_history.append((balance,amount))
        print(f'Withdrawed {amount}. The new balance is {balance}')
    else:
        print("Insufficient funds")
        
    return balance

def check_balance(balance):
    print(f'Balance is {balance}')




balance = 0
pin_code = 4344
tr_history = []

for i in range(2):
    print("Write the pin code (****)")
    pinchoice = int(input())
    if pinchoice == pin_code:
        while(True):
            print(
'''
==============================
 BANKING SYSTEM
==============================
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Exit
==============================''')
            print("Choose an option: ")
            choice = int(input())
            if choice == 1:
                print("Enter amount to deposit: ")
                amount = int(input())
                balance = deposit(balance, amount,tr_history)
            elif choice == 2:
                print("Enter amount to withdraw: ")
                amount = int(input())
                balance = withdraw(balance, amount,tr_history)
                print(tr_history)
            elif choice == 3:
                print("The balance: ")
                check_balance(balance)
            elif choice == 4:
                break
            else:
                print("Wrong choice")
    else:
        print("Try again")

            
        
        