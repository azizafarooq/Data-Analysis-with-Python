import pandas as pd

data = {
    'id': [1, 2, 3],
    'Unnamed: 0': [0, 1, 2],
    'price': [300000, 450000, 350000],
    'sqft_living': [1500, 2500, 2000],
    'floors': [1, 2, 1],
    'waterfront': [0, 1, 0]
}
df = pd.DataFrame(data)

df_dtypes = df.dtypes
print(df_dtypes)
