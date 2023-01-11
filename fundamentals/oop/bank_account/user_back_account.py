from bank_acct_pkg.user import User

# TESTING USER USER & BANKACCOUNT CLASS #
user_1 = User("Stephanie", "steph23grasso@gmail.com").open_account("Savings")
user_2 = User("Joe", "joedudeguy@gmail.com").open_account("Savings")

user_1.make_deposit(2000, "Checking").make_deposit(4000, "Savings")
user_1.open_account("Secret Stash", .05, 20000000)
user_1.make_deposit(50, "Secret Stash")

user_1.make_withdraw(1000, "Checking").make_withdraw(1500, "Savings")
user_1.transfer_money(200, user_2, "Checking", "Checking")

user_1.display_user_balance()
user_2.display_user_balance()