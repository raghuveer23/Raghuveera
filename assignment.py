import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("cars.csv")
df = pd.DataFrame(data)
price = df["Price"].head(10)
cars = df["Model Name"].head(10)
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(price, labels=cars, explode=explode, shadow=True, autopct='%1.1f%%')
plt.title("Cars and their price")
plt.show()