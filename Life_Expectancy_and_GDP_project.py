
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('all_data.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Display summary statistics
print(df.describe())

# Visualize life expectancy over time for the six nations
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Year', y='Life expectancy at birth (years)', hue='Country')
plt.title('Life Expectancy Over Time')
plt.xlabel('Year')
plt.ylabel('Life Expectancy (years)')
plt.legend(loc='best')
plt.show()

# Visualize GDP over time for the six nations
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Year', y='GDP', hue='Country')
plt.title('GDP Over Time')
plt.xlabel('Year')
plt.ylabel('GDP (USD)')
plt.legend(loc='best')
plt.show()

# Correlation between GDP and life expectancy
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='GDP', y='Life expectancy at birth (years)')
plt.title('Correlation between GDP and Life Expectancy')
plt.xlabel('GDP (USD)')
plt.ylabel('Life Expectancy (years)')
plt.show()

# Average life expectancy in the six nations
avg_life_expectancy = df.groupby('Country')['Life expectancy at birth (years)'].mean()
print('Average Life Expectancy:')
print(avg_life_expectancy)

# Distribution of life expectancy
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Life expectancy at birth (years)', bins=20, kde=True)
plt.title('Distribution of Life Expectancy')
plt.xlabel('Life Expectancy (years)')
plt.ylabel('Frequency')
plt.show()

