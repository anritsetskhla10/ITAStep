# Football Team Managmenet System

# შექმენით კლასი FootballTeam შემდეგი ატრიბუტებით:
# team_name (string) - კლუბის სახელი
# coach (string) - მწვრთნელი
# players - მოთამაშეების სია(შექმნისას ცარიელი უნდა იყოს)

# კლასს უნდა გააჩნდეს შემდეგი მეთოდები:
# 1. მოთამაშის დამატება - მოთამაშის სახელი, პოზიცია, სათამაშო ნომერი, 
#    ასაკი და ეროვნება(დიქტის სახით უნდა დაემატოს მოთამაშეების სიაში)

# 2. მოთამაშის წაშლა - მოთამაშე უნდა წაიშალოს სიიდან სათამაშო ნომრის მიხედვით

# 3. მოთამაშის ინფორმაციის განახლება - მოთამაშე უნდა მონახოთ სათამაშო ნომრის მიხედვით
#    და უნდა დაუსეტოთ ისეთი ინფორმაცია, რომელსაც გადასცემთ ამ მეთოდს, მაგ: "goal": 1 
#    ანუ key და value უნდა იყოს გადაცემული ამავე მეთოდის გამოძახებისას!

# 4. კლუბის ინფორმაციის ჩვენება - გამოიტანეთ კლუბის სახელი, მწვრთნელის სახელი და მოთამაშეების სია

# 5. მოთამაშის ინფორმაციის ჩვენება - უნდა გამოიტანოთ ინფორმაცია მოთამაშის ნომრის მიხედვით


class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, name, position, number, age, nationality):
        player = {
            "name": name,
            "position": position,
            "number": number,
            "age": age,
            "nationality": nationality
        }
        self.players.append(player) 
    
    def remove_player(self, number):
        self.players = [player for player in self.players if player["number"] != number]
    
    def update_player_info(self, number, key, value):
        for player in self.players:
            if player["number"] == number:
                player[key] = value
                break

    def show_team_info(self):
        print(f"Team Name: {self.team_name}")
        print(f"Coach: {self.coach}")
        print("Players:")
        for player in self.players:
            print(player)

    def show_player_info(self, number):
        for player in self.players:
            if player["number"] == number:
                print(f"Player Info: {player}")
                break

my_team = FootballTeam("Georgia National Team", "Willy Sagnol")

my_team.add_player("Giorgi Mamardashvili", "Goalkeeper", 1, 25, "Georgian")
my_team.add_player("Khvicha Kvaratskhelia", "Forward", 7, 25, "Georgian")
my_team.add_player("Otar Kiteishvili", "Midfielder", 17, 30, "Georgian")

my_team.update_player_info(7, "goals", 15)
    
my_team.remove_player(1)

my_team.show_team_info()

my_team.show_player_info(7)
    