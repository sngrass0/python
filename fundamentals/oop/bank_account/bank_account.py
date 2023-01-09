class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = .02, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee ")
            self.balance -= 5
        return self
        
    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        if (self.balance > -1):
            self.balance += self.balance * self.int_rate
        return self

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

# TESTING BANKACCOUNT CLASS #
user_1 = BankAccount(.05, 7000)
user_2 = BankAccount(.03, 50050)

user_1.deposit(100).deposit(200).deposit(300).withdraw(100).yield_interest().display_account_info()
user_2.deposit(200).deposit(400).withdraw(80).withdraw(30).withdraw(10).withdraw(12000).yield_interest().display_account_info()

BankAccount.all_balances()