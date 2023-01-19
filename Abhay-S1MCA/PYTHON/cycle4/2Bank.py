from random import randint

class Bank:
    def __init__(self, acc_no, name, acc_type ):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = 0
    
    def display(self):
        print("***************************")
        print("Name : ", name)
        print("Account No : ", acc_no)
        print("Account Type : ", acc_type)
        print("***************************")
    

    def view_balance(self):
        print("Balance = ", self.balance)

    def deposit(self):
        amt = int(input("Enter Amount to Deposit : "))
        self.balance += amt
        self.view_balance()

    def withdraw(self):
        amt = int(input("Enter Amount to Withdraw : "))
        if amt > self.balance:
            print("\nInsufficient Balance")
            return

        self.balance -= amt
        print("\nRs ", amt, "Withdrawn" )
        self.view_balance()

name = input("Enter User Name : ")
acc_no = randint(11111, 99999)
acc_type = input("Enter Account Type : ")

ob1 = Bank(acc_no, name, acc_type)
ob1.display()

while True:
    print("---------------------\n")
    print("1.Deposit\n2.Withdraw\n3.Exit")
    c = int(input("Enter Selection : "))

    if c == 1:
        ob1.deposit()
    elif c == 2: 
        ob1.withdraw()
    elif c == 3:
        break
    else:
        print("Invalid Choice")
        
    
