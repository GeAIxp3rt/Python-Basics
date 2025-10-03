import pandas as pd

music = {
    "Track": ["Beat 1", "Beat 2", "Beat 3"],
    "Duration(min)": [3.5, 4.0, 2.8]
}

df_music = pd.DataFrame(music)
print(df_music)