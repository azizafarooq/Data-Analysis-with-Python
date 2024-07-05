features = ["floors", "waterfront", "lat", "bedrooms", "sqft_basement", 
            "view", "bathrooms", "sqft_living15", "sqft_above", "grade", "sqft_living"]


data = {
    'price': [300000, 450000, 350000],
    'floors': [1, 2, 1],
    'waterfront': [0, 1, 0],
    'lat': [47.5, 47.6, 47.7],
    'bedrooms': [3, 4, 3],
    'sqft_basement': [500, 0, 300],
    'view': [0, 1, 0],
    'bathrooms': [1.5, 2.5, 2],
    'sqft_living15': [1500, 2500, 2000],
    'sqft_above': [1000, 2000, 1500],
    'grade': [7, 9, 8],
    'sqft_living': [1500, 2500, 2000]
}
df = pd.DataFrame(data)

X = df[features]
y = df['price']
lm.fit(X, y)
y_pred = lm.predict(X)
r2 = r2_score(y, y_pred)
print(f'R^2: {r2}')
