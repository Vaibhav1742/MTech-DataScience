import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('prices.csv')
print(df)
plt.xlabel('area')
plt.ylabel('prices')
plt.scatter(df.area,df.price,color="red")
plt.show()

reg = linear_model.LinearRegression()
reg.fit(df[['area']],df[['price']])
print(reg.predict([[3300]]))

# y = bo + b1x
# predict y =
print(reg.coef_)    # b1
print(reg.intercept_)  #bo
print(reg.intercept_ + reg.coef_ * 3300)

