import pandas as pd

df = pd.read_csv("players_data_light-2024_2025.csv")
print(df.head())

print(df.describe())
print(df["Gls"].mean())
print(df[df["Gls"] > 24])

total_goals = df["Gls"].sum()
best_player = df.loc[df["Gls"].idxmax()]

print("Total Goals:", total_goals)
print("Best Player:", best_player)