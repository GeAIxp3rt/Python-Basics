import pandas as pd

data = {
    "Player": ["Mario", "Cristi", "Robert", "Dragos"],
    "Goals": [5, 7, 3, 6],
    "Assists": [2, 1, 4, 3]
}

df = pd.DataFrame(data)
print(df)