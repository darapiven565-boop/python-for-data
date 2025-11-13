import pandas as pd

url = "data/movies_metadata.csv"

df = pd.read_csv(url)

# print(df.head())
# df.info()
# print(df.describe())
# print(df.isnull().sum())
# print(df[["belongs_to_collection", "homepage", "tagline"]])

# df["tagline"].fillna("without tagline", inplace=True) #застарілий

# # нові альтернативи старому варіанту
# df.fillna({"tagline" : "without tagline"}, inplace=True)
df["tagline"] = df["tagline"].fillna("without tagline")

# print(df["tagline"])
df["homepage"] = df["homepage"].fillna("no homepage")
# print(df["homepage"])

df.fillna({"belongs_to_collection" : "{}"}, inplace=True)
# print(df.belongs_to_collection)
# df.info()

df.dropna(inplace=True)
print(df.isnull().sum())