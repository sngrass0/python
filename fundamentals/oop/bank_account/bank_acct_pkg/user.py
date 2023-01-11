from bank_acct_pkg.bank_account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {
            "Checking" : BankAccount(int_rate=0.02, balance=0)
        }
    
    def open_account(self, account_name, int_rate=0.02, initial_balance=0):
        if self.accounts.get(account_name) != None:
            print("Account with that name already exists")
        else:
            self.accounts[account_name] = BankAccount(int_rate, initial_balance)
        return self
    
    def make_deposit(self, amount, account):
        if self.accounts.get(account) == None:
            print("No account found")
        else:
            self.accounts[account].deposit(amount)
        return self
    
    def make_withdraw(self, amount, account):
        if self.accounts.get(account) == None:
            print("No account found")
        else:
            self.accounts[account].withdraw(amount)
        return self

    def display_user_balance(self):
        for account in self.accounts:
            print(f"User: {self.name}, {account} Balance: {self.accounts[account].balance}")
        return self
    
    def transfer_money(self, amount, other_user, acc_1, acc_2):
        if not BankAccount.can_withdraw(self.accounts[acc_1].balance, amount):
            print("Not enough funds to transfer money")
        elif other_user.accounts.get(acc_2) == None:
            print("could not find account")
        else:
            self.accounts[acc_1].withdraw(amount)
            other_user.accounts[acc_2].deposit(amount)
        return self