import pandas as pd
month = ["Jan", "Feb", "Mar", "Apr"]
sales = {
    "revenue" : [100, 200, 300, 400],
    "items_sold" : [23, 43, 54, 65],
    "new_clients" : [10, 20, 30, 40]
}

df = pd.DataFrame(data=sales, index=month)
# print(df)

# vector = [1, 2, 3]
# print(vector * 2)

# series = pd.Series([1, 2, 3])
# print(series * 2)

# series_str = pd.Series(["a", "b", "c"])
# print(series_str[0])

# month = ["Jan", "Feb", "Mar", "Apr"]
# sales = [100, 200, 300, 400]
# data = pd.Series(data=sales, index=month)
# print(data)
# print(data["Feb"])

# print(df.head(2))
# print(df.tail(1))

# print(df.revenue)

# print(df.shape) #повертає кортежем (рядки, стовпчики)
# print(df.columns)
# print(df.describe()) #статистика по числовим стовпчикам
# print(df.dtypes)

df.revenue = ["100", "200", "300", "400"]
# print(df.revenue.dtypes)
df.revenue = pd.to_numeric(df.revenue, errors="coerce") #зміна типу і обробка помилки якщо є не число
# # print(df.describe())
# print(df.revenue.dtypes)

# print(df.loc["Feb"])

movies_df = pd.read_csv("data/movies_metadata.csv")
# print(movies_df.sample(3))
# print(movies_df.to_string())
pd.options.display.max_rows = 10
print(pd.options.display.max_rows)
