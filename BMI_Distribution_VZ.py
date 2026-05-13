import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = r'C:\Users\Abobus\OneDrive\Рабочий стол\fitness_dataset.csv'

try:
    df = pd.read_csv(file_path)
    print("CSV was succesfully loaded!")
except FileNotFoundError:
    print(f"CSV was not found {file_path}.")
    exit()

overweight_count = len(df[df['bmi'] > 25])
total_count = len(df)
percentage = (overweight_count / total_count) * 100

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

sns.histplot(df['bmi'], bins=50, kde=True, color='#4CABA1', stat="density", alpha=0.6)

plt.axvline(x=25, color='red', linestyle='--', linewidth=2)

plt.text(25.5, 0.08, f'BMI 25.0 ({percentage:.1f}% Overweight)',
         color='red', fontweight='bold', fontsize=12)

plt.title('BMI Distribution', fontsize=16, pad=15)
plt.xlabel('BMI', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.xlim(10, 45)
plt.tight_layout()

plt.show()
