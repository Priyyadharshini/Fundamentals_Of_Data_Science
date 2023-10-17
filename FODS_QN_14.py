import pandas as pd
import matplotlib.pyplot as plt

data = {'age': [23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61],
        '%fat': [9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]}
df = pd.DataFrame(data)

age_mean = df['age'].mean()
age_median = df['age'].median()
age_std = df['age'].std()

fat_mean = df['%fat'].mean()
fat_median = df['%fat'].median()
fat_std = df['%fat'].std()

print("Age - Mean: ", age_mean, " Median: ", age_median, " Standard Deviation: ", age_std)
print("%fat - Mean: ", fat_mean, " Median: ", fat_median, " Standard Deviation: ", fat_std)

df.boxplot(column=['age', '%fat'])
plt.show()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(df['age'], df['%fat'])
plt.xlabel('Age')
plt.ylabel('%fat')
plt.title('Scatter plot of Age vs %fat')

plt.subplot(1, 2, 2)
import scipy.stats as stats
import pylab

stats.probplot(df['age'], dist="norm", plot=pylab)
plt.title('Q-Q plot for Age')
plt.show()

