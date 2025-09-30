players = ["Dragoș", "Angel", "Mario", "Cristi"]

def team_score(players):
    score = 0
    for player in players:
        if player == "Dragoș":
            score += 10
        else:
            score += 5
    return score

print("Team Score:", team_score(players))