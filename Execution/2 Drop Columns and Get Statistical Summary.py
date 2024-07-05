df.drop(columns=['id', 'Unnamed: 0'], inplace=True)

df_summary = df.describe()
print(df_summary)
