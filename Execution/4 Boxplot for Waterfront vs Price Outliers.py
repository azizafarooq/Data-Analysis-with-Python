import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x='waterfront', y='price', data=df)
plt.title('Waterfront vs Price Outliers')
plt.show()
