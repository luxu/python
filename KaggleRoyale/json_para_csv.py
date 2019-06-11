import pandas as pd

file_name = u'players.csv'

df = pd.read_json('players.json')

df.to_csv(file_name, encoding='utf-8', index=False)
