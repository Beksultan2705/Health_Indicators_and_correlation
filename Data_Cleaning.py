import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


file_path = r'C:\Users\Abobus\OneDrive\Рабочий стол\fitness_dataset.csv'

try:
    df = pd.read_csv(file_path)
    print("✅ DataSet has been found!")
except FileNotFoundError:
    print("❌ DataSet was not found")
    exit()

df = df.drop_duplicates()

if df.isnull().values.any():
    df = df.fillna(df.mean(numeric_only=True))

df = df[(df['heart_rate_resting'] >= 40) & (df['heart_rate_resting'] <= 200)]

df['steps_per_active_min'] = df['steps_per_day'] / df['active_minutes']

plt.figure(figsize=(12, 10))

numeric_df = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='RdYlGn', fmt='.2f', linewidths=0.5)
plt.title('How are health indicators related to each other')
plt.tight_layout()
plt.show()

print("\n--- Main indicators after Data_cleaning ---")
print(df[['age', 'steps_per_day', 'sleep_hours', 'stress_level']].describe())
