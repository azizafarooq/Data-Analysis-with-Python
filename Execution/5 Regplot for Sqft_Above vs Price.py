df['sqft_above'] = [1000, 2000, 1500]

sns.regplot(x='sqft_above', y='price', data=df)
plt.title('Sqft_Above vs Price')
plt.show()
