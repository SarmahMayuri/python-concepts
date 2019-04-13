class Bank_Account():

    def __init__(self,owner,balance):
        self.owner= owner
        self.balance= balance

    def deposit(self,amount):
        self.balance= self.balance + amount
        print(f'Your account is deposited with an amount of ${amount} and the current balance is ${self.balance}')

    def withdraw(self,amount):
        if amount>self.balance:
            print('Funds unavailable!')
        else:
            self.balance= self.balance - amount
            print(f'Your account has been withdrawn an amount of ${amount} and the current balance is ${self.balance}')

    def __str__(self):
        return (f'Hello {self.owner}! Your current balance is ${self.balance}')


account1= Bank_Account('Mayuri Sarmah', 100)
print(account1)
print(account1.owner)
print(account1.balance)
account1.deposit(100)
account1.withdraw(50)
account1.withdraw(250)
