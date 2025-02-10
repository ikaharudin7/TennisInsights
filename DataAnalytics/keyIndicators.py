import pandas as pd
import numpy as np
import sklearn
import csv
from pathlib import Path
import os
import plotly.express as px
from shiny import App, render, ui
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import zscore

# Analyse what are the key statistics a player needs to win in a match to win on each of the 3 surfaces
# Model be trained on top players historically over each surface, at a grand slam. 
# Predictions will happen based on the inputs of key match statistics, based on player's averages for the last season on that surface. 

# Extract match CSVs
clayMatchData = pd.DataFrame

path = Path("/ATPMatchData/")
main_df = pd.DataFrame()

for year in os.listdir('DataAnalytics/ATPMatchData'):
    if year.endswith('.csv'):
        file_path = os.path.join('DataAnalytics/ATPMatchData', year)
        df = pd.read_csv(file_path)
        main_df = pd.concat([main_df, df], ignore_index=True)

# DATA CLEANING AND TRANSFORMATION
# __________________________________________________________________________________________________________________________
# 2ND SERVE POINTS WON
clay_df = main_df[main_df['surface'] == 'Clay']
clay_df = clay_df[clay_df['tourney_date'] > 20080000]

feature_df = pd.DataFrame()
feature_df['1st_srv_diff'] = clay_df['w_1stWon'] - clay_df['l_1stWon']
feature_df['2nd_srv_diff'] = clay_df['w_2ndWon'] - clay_df['l_2ndWon']
feature_df['bp_saved_diff'] = clay_df['w_bpSaved'] - clay_df['l_bpSaved']
feature_df['1st_srv_won_diff'] = clay_df['w_1stWon'] - clay_df['l_1stWon']
feature_df['2nd_srv_won_diff'] = clay_df['w_2ndWon'] - clay_df['l_2ndWon']

# Hardcourt tournament data cleaning
hard_df = main_df[main_df['surface'] == 'Hard']
hard_df = hard_df[hard_df['tourney_date'] > 20080000]

feature_h_df = pd.DataFrame()
feature_h_df['1st_srv_diff'] = hard_df['w_1stWon'] - hard_df['l_1stWon']
feature_h_df['2nd_srv_diff'] = hard_df['w_2ndWon'] - hard_df['l_2ndWon']
feature_h_df['bp_saved_diff'] = hard_df['w_bpSaved'] - hard_df['l_bpSaved']
feature_h_df['1st_srv_won_diff'] = hard_df['w_1stWon'] - hard_df['l_1stWon']
feature_h_df['2nd_srv_won_diff'] = hard_df['w_2ndWon'] - hard_df['l_2ndWon']

# Grass tournament data cleaning
grass_df = main_df[main_df['surface'] == 'Grass']
grass_df = grass_df[grass_df['tourney_date'] > 20080000]

feature_g_df = pd.DataFrame()
feature_g_df['1st_srv_diff'] = grass_df['w_1stWon'] - grass_df['l_1stWon']
feature_g_df['2nd_srv_diff'] = grass_df['w_2ndWon'] - grass_df['l_2ndWon']
feature_g_df['bp_saved_diff'] = grass_df['w_bpSaved'] - grass_df['l_bpSaved']
feature_g_df['1st_srv_won_diff'] = grass_df['w_1stWon'] - grass_df['l_1stWon']
feature_g_df['2nd_srv_won_diff'] = grass_df['w_2ndWon'] - grass_df['l_2ndWon']

# Get rid of NAN values
feature_df = feature_df.dropna()
feature_h_df = feature_h_df.dropna()
feature_g_df = feature_g_df.dropna()

# Calculate the z-score for each feature to be graphed - 1st serve points
feature_df['zscore_1st'] = zscore(feature_df['1st_srv_won_diff'])
feature_h_df['zscore_1st'] = zscore(feature_h_df['1st_srv_won_diff'])
feature_g_df['zscore_1st'] = zscore(feature_g_df['1st_srv_won_diff'])

# Calculate the z-score for each feature to be graphed - 2nd serve points
feature_df['zscore_2nd'] = zscore(feature_df['2nd_srv_won_diff'])
feature_h_df['zscore_2nd'] = zscore(feature_h_df['2nd_srv_won_diff'])
feature_g_df['zscore_2nd'] = zscore(feature_g_df['2nd_srv_won_diff'])

# Identify outliers with a z-score greater than 3 Sdevs, and remove them from the average
threshold = 3

first_clay = feature_df[feature_df['zscore_1st'] < threshold]
first_hard = feature_h_df[feature_h_df['zscore_1st'] < threshold]
first_grass = feature_g_df[feature_g_df['zscore_1st'] < threshold]

second_clay = feature_df = feature_df[feature_df['zscore_2nd'] < threshold]
second_hard = feature_h_df[feature_h_df['zscore_2nd'] < threshold]
second_grass = feature_g_df[feature_g_df['zscore_2nd'] < threshold]

print(feature_g_df)
#___________________________________________________________________________________________________________________________________
# Display the data with Shiny
# Nest Python functions to build an HTML interface
app_ui = ui.page_fluid( # Layout the UI with Layout Functions
 
  #  Add Inputs with ui.input_*() functions 
  ui.h2("Serve Statistics - Winner to Loser Average Differentials (ATP Tour Matches 2008-2024)"),
    ui.output_plot("barGraph1st"),
  ui.output_plot("barGraph2nd")
  # Add Outputs with ui.ouput_*() functions
)

def server(input, output, session):
    BAR_WIDTH = 0.4
    @output
    @render.plot
    def barGraph1st():
      fig, ax = plt.subplots()
      ax.bar(width=BAR_WIDTH, x=['Grass Court', 'Hard Court', 'Clay Court'], height=[first_grass['1st_srv_won_diff'].mean(), first_hard['1st_srv_won_diff'].mean(), first_clay['1st_srv_won_diff'].mean()], )
      ax.set_title('1st Serve Points Won Differential on Different Surfaces')
      ax.set_ylabel('Differential (winner - loser)')
      
      return fig
    @render.plot
    def barGraph2nd():
      fig, ax = plt.subplots()
      ax.bar(width=BAR_WIDTH, x=['Grass Court', 'Hard Court', 'Clay Court'], height=[second_grass['2nd_srv_won_diff'].mean(), second_hard['2nd_srv_won_diff'].mean(), second_clay['2nd_srv_won_diff'].mean()])
      ax.set_title('2nd Serve Points Won Differential on Different Surfaces')
      ax.set_ylabel('Differential (winner - loser)')
      
      return fig
    



app = App(app_ui, server)

if __name__ == "__main__":
    app.run()




# Standardise the metrics e.g. BPs won/converted or Serve rating or UE rating. Each one will become a feature which determines an outcome.
# Take the features of the winning players, and label them as win, and the features of losing players and label them as a loss


# Train the models

# Pred