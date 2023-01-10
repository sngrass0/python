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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = { 
            "Checking" : BankAccount(int_rate=0.02, balance=0), 
            "Saving" : BankAccount(int_rate=0.02, balance=0) 
        }
    
    def make_deposit(self, amount, account):
        if(self.accounts.get(account) == None):
            print("No account found")
        else:
            self.accounts[account].deposit(amount)
        return self
    
    def make_withdraw(self, amount, account):
        if(self.accounts.get(account) == None):
            print("No account found")
        else:
            self.accounts[account].withdraw(amount)
        return self

    def display_user_balance(self):
        for account in self.accounts:
            print(f"User: {self.name}, {account} Balance: {self.accounts[account].balance}")
        return self
    
    def transfer_money(self, amount, other_user):
        other_user.accounts["Checking"].deposit(amount)
        return self


# TESTING USER BANKACCOUNT CLASS #

user_1 = User("Stephanie", "steph23grasso@gmail.com")
user_2 = User("Joe", "joedudeguy@gmail.com")

user_1.make_deposit(2000, "Checking").make_deposit(4000, "Saving")
user_1.make_withdraw(1000, "Checking").make_withdraw(1500, "Saving")
user_1.transfer_money(200, user_2)

user_1.display_user_balance()
user_2.display_user_balance()