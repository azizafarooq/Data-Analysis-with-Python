from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = df[['sqft_living']]
y = df['price']
lm = LinearRegression()
lm.fit(X, y)
y_pred = lm.predict(X)
r2 = r2_score(y, y_pred)
print(f'R^2: {r2}')
