class Account():

    def __init__(self):
        self.balance = 100
        self.currency = 'RM'
        # self.accepted_amt = (10, 20, 50, 100, 200)

    def deposit(self, amount=None):
        amount = int(input("Enter amount to be Deposited: "))
        self.balance = self.balance + amount
        if amount % 10 == 0 or amount % 5 == 0:
            # if amount in self.accepted_amt:
            print(f'Your new balance is: {self.currency}{self.balance}')
        else:
            print('Please enter a valid amount')

    def withdraw(self, amount=None):
        amount = int(input("Enter amount to Withdraw: "))
        self.balance = self.balance - amount
        # if amount in self.accepted_amt and self.balance > 0:
        if self.balance < amount:
            print('You have insufficient funds')
        elif amount % 10 == 0 or amount % 5 == 0:
            print(f'Your new balance is: {self.currency}{self.balance}')
        else:
            print('Please withdraw a valid amount')


acc_holder_san = Account()
answer = input("Enter deposit or withdraw: ")
if answer == "deposit":
    acc_holder_san.deposit()
else:
    acc_holder_san.withdraw()
