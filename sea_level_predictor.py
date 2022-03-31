import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
  plt.scatter(df['Year'] , df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
  linregress_output = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  
  slope = linregress_output.slope
  y_intercept=linregress_output.intercept
  
  axe_X=np.arange(df['Year'].min(),2050,1)
  axe_Y=slope*axe_X + y_intercept

  plt.plot(axe_X,axe_Y)
  
    # Create second line of best fit
  linregress_output2 = linregress(df.loc[df['Year']>=2000 , 'Year'], df.loc[df['Year']>=2000,'CSIRO Adjusted Sea Level'])
  
  slope_2000 = linregress_output2.slope
  y_intercept_2000=linregress_output2.intercept

  axe_X_sup_2000=np.arange(2000,2050,1)
  axe_Y_2000=slope_2000*axe_X_sup_2000 + y_intercept_2000

  plt.plot(axe_X_sup_2000,axe_Y_2000)

    # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
  

    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()