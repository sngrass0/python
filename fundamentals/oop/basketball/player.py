class Player:
    def __init__(self, data):
        # CHALLENGE 1
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)
        print("====================")
        return self
    
    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for player in team_list:
            new_team.append(Player(player))
        return new_team

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

    
# CHALLENGE 2
player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)

# CHALLENGE 3
new_team = []
for player in players:
    new_team.append(Player(player))

# BONUS CHALLENGE
new_new_team = Player.get_team(players)
for player in new_new_team:
    player.display_info()

