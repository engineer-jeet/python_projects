class Customer:
    '''This class is developed by Jeet and it describes bank operations.'''
    bankname = "Bharat_Tech_Bank"

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.balance += amount
        print("After deposit, Balance is:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if amount > self.balance:
            print("Insufficient Funds!")
        else:
            self.balance -= amount
            print("After withdrawal:", self.balance)


print("Welcome to", Customer.bankname)

name = input("Enter your name: ")
c = Customer(name)

while True:
    print('\nd-Deposit\nw-Withdraw\nb-Balance\ne-Exit')
    option = input('Choose your option: ').lower()

    if option == 'd':
        try:
            amount = float(input("Enter amount to deposit: "))
            c.deposit(amount)
        except ValueError:
            print("Invalid input! Enter a number.")

    elif option == 'w':
        try:
            amount = float(input("Enter amount to withdraw: "))
            c.withdraw(amount)
        except ValueError:
            print("Invalid input! Enter a number.")

    elif option == 'b':
        print("Current balance:", c.balance)

    elif option == 'e':
        print("Thanks For Banking With Us!")
        break

    else:
        print("Invalid option. Try again.")