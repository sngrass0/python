class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("First Name:\t", self.first_name)
        print("Last Name:\t", self.last_name)
        print("email:\t", self.email)
        print("age:\t", self.age)
        print("Rewards member?:", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points)
        return self
    
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self
    
    def spend_points(self,amount):
        if amount > self.gold_card_points: 
            print("Not enough gold points :(")
        else:
            self.gold_card_points -= amount
        return self

# TESTING USER CLASS METHODS #
user_1 = User("Stephanie", "Grasso", "steph23grasso@gmail.com", 23)
user_2 = User("John", "Stone", "johnstone@gmail.com", 55)
user_3 = User("Trevor", "Virtue", "trevorrrr@gmail.com", 31)

users = [user_1, user_2, user_3]

user_1.display_info().enroll().spend_points(50)

user_2.enroll().spend_points(80)

print()
for user in users:
    user.display_info()
    print("--------------------------")

user_1.enroll()

user_3.spend_points(40)


