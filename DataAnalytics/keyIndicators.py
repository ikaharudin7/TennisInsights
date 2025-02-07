import pandas as pd
import numpy as np
import sklearn
import csv
from pathlib import Path
import os

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
print(clay_df)

# Take the differential between 