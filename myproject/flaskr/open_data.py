import pandas as pd
import json
import sqlalchemy as sa

with open("venue_data1.json") as f:
    data = json.load(f)
df = pd.DataFrame(data)
# print(df.head())
# print(df.columns)


engine = sa.create_engine('postgresql:///fyyur_database')

df.to_sql('venue', engine, if_exists='replace', index=False)
with open("artist_data1.json") as f:
    artist_data = json.load(f)
df = pd.DataFrame(artist_data)


df.to_sql('artist', engine, if_exists='replace', index=False)


