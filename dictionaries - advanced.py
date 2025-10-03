team = {"Geaner": "Coach", "Cristi": "Striker", "Angel": "Defender"}

print(team.keys())
print(team.values())

team["Dragos"] = "Goalkeeper"
del team["Cristi"]

print(team)