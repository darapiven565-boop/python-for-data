import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "data/imdb_tv_ranking_master.csv"
df = pd.read_csv(url)
# print(df.describe())
# print(df.isnull().sum())
# print(df.head())
# print(df.info())
df.fillna({"end_year" : "ongoing"}, inplace=True)
# df.dropna(inplace=True)
print(df.isnull().sum())
print(df["title_id"])

