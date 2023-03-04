import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv', index_col='Year')

    # Create scatter plot
  fig, ax = plt.subplots(figsize=(12,6))
  plt.scatter(df.index, df['CSIRO Adjusted Sea Level'], c='blue', s=15)

    # Create first line of best fit
  reg1 = linregress(df.index, df['CSIRO Adjusted Sea Level'])
  x1 = np.arange(df.index.min(),2050,1)
  plt.plot(x1, reg1.intercept + reg1.slope*x1, 'r')

    # Create second line of best fit
  df2 = df[df.index >= 2000]
  reg2 = linregress(df2.index, df2['CSIRO Adjusted Sea Level'])
  x2 = np.arange(df2.index.min(),2050,1)
  plt.plot(x2, reg2.intercept + reg2.slope*x2, 'g')

    # Add labels and title
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")
  
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
