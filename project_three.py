class Account:
    def __init__(self, bal, acc, pin):
        self.balance = bal
        self.account_no = acc
        self.pin = pin
    def debit(self, amount):
        self.balance = self.balance-amount
        print("Rs.", amount, "was debited")
        print("Remaning balance is", self.check_balance())
    def credit(self, amount):
        self.balance = self.balance+amount
        print("Rs.", amount, "was credited")
        print("Total balance is", self.check_balance())
    def check_balance(self):
        return self.balance


balance = int(input("Enter initial balance : "))
account_no = (input("Enter account number : "))
pin = int(input("Enter pin : "))
acc1 = Account(balance, account_no, pin)
print("Account created successfuly!")

login_pin = int(input("Enter your PIN to login : "))

if (login_pin == acc1.pin):
    print("Login successfull")
    print()
    choice = 0
    while choice != 4:
        print("MENU-:")
        print("1.Check balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        choice = int(input("Enter your choice : "))

        if(choice == 1):
            print(acc1.check_balance())
        elif(choice == 2):
            deposit = int(input("Enter deposit amount : "))
            acc1.credit(deposit)
        elif(choice == 3):
            withdraw = int(input("Enter amount to withdraw : "))
            acc1.debit(withdraw)
        
    print("ATM closed")
    
else:
    print("Incorrect pin")

