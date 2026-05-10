import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r'C:\Users\Abobus\OneDrive\Рабочий стол\fitness_dataset.csv'

try:
    df = pd.read_csv(file_path)

    sns.set_theme(style="whitegrid")

    fitness_summary = df.groupby('fitness_level')[['steps_per_day', 'sleep_quality', 'stress_level', 'bmi']].mean()
    print("\n--- Average Metrics by Fitness Level ---")
    print(fitness_summary)

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='sleep_hours', y='stress_level', hue='fitness_level', palette='viridis', alpha=0.7)
    plt.title('Stress Level vs. Sleep Hours')
    plt.xlabel('Sleep Hours')
    plt.ylabel('Stress Level')
    # Fixed: added explicit location to avoid the warning
    plt.legend(title='Fitness Level', loc='upper right')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(df['bmi'], bins=20, kde=True, color='skyblue')
    plt.title('BMI Distribution')
    plt.axvline(25, color='red', linestyle='--', label='Normal Weight Limit (25)')
    # Fixed: added explicit location
    plt.legend(loc='upper right')
    plt.show()

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except KeyError as e:
    print(f"Error: Missing column in dataset: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
