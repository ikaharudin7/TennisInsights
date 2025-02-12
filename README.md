# Professional Tennis Insights
This project contains data analysis and Machine-Learning techniques on professional tennis (ATP Tour) data from 1968 to present. Data is taken from this GitHub Repository: https://github.com/JeffSackmann/tennis_atp/tree/master, and was also data scraped from tennisabstract.com by a Python script.

Please take a look at the more interesting insights which I have gathered in this project - from someone with a heavy interest in tennis! Graphics are created using Shiny, pyplot and matplotlib, using a combination of Python and R. This project is in progress, and will continue to be updated as I work towards uncovering the characteristics that make a great tennis player at ATP level. 

## 1. Average age of ATP Tour match winners from 2010-2024
![image](https://github.com/user-attachments/assets/b6fe98e0-f377-4a41-8e10-04a08da3b2f9)

Every year in November/December, there is a consistent drop in the average age of match winners.
This is due to the Under 21 ATP NEXTGEN Finals tournament that occurs during that time.
2015-2017 was the peak of the Big 4 Era, with veterans hitting near 30 during those years.
Average age has declined since, due to the emergence of NEXTGEN players Alcaraz, Sinner, Ruud, Medvedev, Tsitsipas

#### Note:
The above graphic was analysed in R, with Shiny and Markdown. 

## 2. Most important rally statistics for Djokovic to win a match (Machine Learning Insights)
![image](https://github.com/user-attachments/assets/6cfc07a2-2eb8-4140-a309-b4e3745b7be0)

Classification Report:
              precision    recall  f1-score   support

           L       0.71      0.73      0.72        30
           W       0.93      0.92      0.93       117

    accuracy                           0.88       147

A machine learning model (random forest classifier) was built based on the data from 750+ Djokovic ATP and Grand Slam Matches (labelled data). This model predicts which key statistics Djokovic will normally require in a match in order to win, and was trained with K-Cross validation. The classification report is listed above, and it predicts outcomes to a high accuracy, however, it may be overfitting a small dataset, as Djokovic only has a finite number of matches he has played. 

The 'vs Ratio' (the ratio of the opponent's winners to unforced errors) was most important of whether Djokovic wins or loses a match. E.g. If opposition had high unforced errors and low winners, Djokovic would likely win the match. Possible explanations for this is Djokovic's playstyle of continuously playing aggressive but high percentage shots, with minimal errors, alongside his elite court coverage and defence. This entices opposition players who struggle to keep up to play more aggressive, low percentage shots, going for winners. However as these shots are hard to execute, this often results in a high unforced error count. 

#### Metrics explained:
- vs Ration: The ratio of the opponent's Winners to Unforced Errors.
- Rally UFE/pt: The percentage of Unforced Errors Djokovic made, excluding ace/double faults.
- UFE/pt: The percentage of Unforced Errors the Djokovic made.
- vs UFE/pt: The percentage of Unforced Errors the opposition (losing) player made.
- vs WNR/pt: The percentage of Winners the opposition (losing) player made.
- Ratio: The ratio of winners to unforced errors of Djokovic.
- RallyRatio: Ratio: The ratio of winners to unforced errors of Djokovic, excluding ace/double faults.
- UFEs: Average number of UFEs Djokovic made.
- FH Wnr/Pt: Percentage of forehand winners Djokovic made.
- Winners: Average number of Winners Djokovic made.
- Rally Wnr/pt: Percentage of winners Djokovic made.
- BH Wnr/pt: Percentage of Backhand winners Djokovic made.

#### Note: 
Machine Learning in Python with Scikit-Learn, and visualised with matplotlib


## 3. Average differentials of 1st and 2nd serve points won on 3 different surfaces
![image](https://github.com/user-attachments/assets/16ae059c-3db5-49da-a8b5-b83884958ac3)
The differentials were calculated by the 1st serve points won by the winner, minus 1st serve points won by the loser, from each ATP match from 2008. Outliers were removed using z-score calculations, and then the values were averaged. 

While no apparent trend is observed with the 1st Serve differential, the 2nd serve differential is largest on clay, the slowest surface. 
This is likely due to the fact that topspin 2nd serves will bounce the highest on clay, making the returner more likely to struggle, as opposed to grass, where the ball won't bounce nearly as much, often falling to the returner's comfortable strike zone.
This heightens the importance of a strong 2nd serve to win matches on clay. 

A possible limitation to this is how the game's speed and surfaces have changed over the years from 2008-2024. Further explorations of this information will be to factor in court speed index, and the evolution of player tactics over the years. 

#### Note:
The above graphic was analysed in Python, with Shiny.


