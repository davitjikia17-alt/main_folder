import pandas as pd
import numpy as np


df = pd.read_excel('Book1.xlsx')


sun_mean = np.mean(df['sunlight'])
sun_median = np.median(df['sunlight'])


height_mean = np.mean(df['height'])
height_median = np.median(df['height'])


date_mean = np.mean(df['date'])
date_median = np.median(df['date'])

print("--- Sunlight ---")
print(f"Mean: {sun_mean}")
print(f"Median: {sun_median}")

print("\n--- Height ---")
print(f"Mean: {height_mean}")
print(f"Median: {height_median}")

print("\n--- Date ---")
print(f"Mean: {date_mean}")
print(f"Median: {date_median}")