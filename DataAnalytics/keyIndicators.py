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


# Clay tournament data cleaning
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

# w_ace,w_df,w_svpt,w_1stIn,w_1stWon,w_2ndWon,w_SvGms,w_bpSaved,w_bpFaced,l_ace,l_df,l_svpt,l_1stIn,l_1stWon,l_2ndWon,l_SvGms,l_bpSaved,l_bpFaced

# Calculate the z-score for each feature to be graphed
#z_clay = np.abs(stats.zscore(feature_df['2nd_srv_won_diff']))
#z_hard = np.abs(stats.zscore(feature_h_df['2nd_srv_won_diff']))

# Identify outliers with a z-score greater than 3, and remove them from the average
threshold = 3
clean_df = pd.DataFrame()
#feature_df = feature_df[z_clay < threshold]
#feature_h_df = feature_h_df[z_hard < threshold]

# Graph it with Shiny
app_ui = ui.page_fluid(
    ui.h2("Clay Court vs Hard Court Winner to Loser Differentials"),
    ui.output_plot("histPlot")
)

# Define server logic
def server(input, output, session):
    @output
    @render.image
    def barGraph():
        fig, ax = plt.subplots()
        # 
        ax.bar(['Hard Court', 'Clay Court'], [feature_h_df['2nd_srv_won_diff'].mean(), feature_df['2nd_srv_won_diff'].mean()])
        ax.set_title('2nd Serve Points Won Differential on Clay vs Hard Court Winners')
        ax.set_xlabel('Surface')
        ax.set_ylabel('Difference between Winner and Loser')
        
        # Return base64 string as image source
        return fig

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()




# Standardise the metrics e.g. BPs won/converted or Serve rating or UE rating. Each one will become a feature which determines an outcome.
# Take the features of the winning players, and label them as win, and the features of losing players and label them as a loss


# Train the models

# Pred