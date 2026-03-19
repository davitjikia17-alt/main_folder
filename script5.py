import pandas as pd
import numpy as np

df = pd.read_excel('Book1.xlsx')

sun_mean = np.mean(df['sunlight'])
sun_median = np.median(df['sunlight'])

height_mean = np.mean(df['height'])
height_median = np.median(df['height'])

date_
