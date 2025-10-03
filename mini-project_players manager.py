team = {"Geaner": "Coach", "Cristi": "Striker"}

while True:
    action = input("Choose: add / remove / view / exit: ")

    if action == "add":
        name = input("Player Name: ")
        role = input("Position: ")
        team[name] = role
        print("Player added:", name)

    elif action == "remove":
        name = input("Player name to delete: ")
        if name in team:
            del team[name]
            print("Player deleted:", name)
        else:
            print("This player is not in the team.")
    
    elif action == "view":
        print("Actual Team:", team)

    elif action == "exit":
        break