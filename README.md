# Professional Tennis Insights
This project contains data analysis and Machine-Learning techniques on professional tennis (ATP Tour) data from 1968 to present. Data is taken from this GitHub Repository: https://github.com/JeffSackmann/tennis_atp/tree/master

Please take a look at the more interesting insights which I have gathered in this project - from someone with a heavy interest in tennis! Graphics are created using Shiny, using a combination of Python and R. 

## Average age of ATP Tour match winners from 2010-2024
![image](https://github.com/user-attachments/assets/b6fe98e0-f377-4a41-8e10-04a08da3b2f9)

Every year in November/December, there is a consistent drop in the average age of match winners.
This is due to the Under 21 ATP NEXTGEN Finals tournament that occurs during that time.
2015-2017 was the peak of the Big 4 Era, with veterans hitting near 30 during those years.
Average age has declined since, due to the emergence of NEXTGEN players Alcaraz, Sinner, Ruud, Medvedev, Tsitsipas

#### Note:
The above graphic was analysed in R, with Shiny and Markdown. 

## Most important rally statistics for Djokovic to win a match (Machine Learning Insights)
![image](https://github.com/user-attachments/assets/6cfc07a2-2eb8-4140-a309-b4e3745b7be0)
A machine learning model (random forest classifier) was built based on the data from 750+ Djokovic ATP and Grand Slam Matches. This model predicts which key statistics Djokovic will normally require in a match in order to win.
vs Ratio (the ratio of the opponent's winners to unforced errors) was most important. If opposition had high unforced errors and low winners, Djokovic would likely win the match. 

Possible explanations for this is Djokovic's playstyle of continuously playing aggressive but high percentage shots, with minimal errors, alongside his elite court coverage and defence. This entices opposition players who struggle to keep up to play more aggressive, low percentage shots, going for winners. However as these shots are hard to execute, this often results in a high unforced error count. 

#### Note: 
Machine Learning in Python with Scikit-Learn, and visualised with matplotlib


## Average differentials (winner minus loser) of 1st and 2nd serve points won on 3 different surfaces
![image](https://github.com/user-attachments/assets/16ae059c-3db5-49da-a8b5-b83884958ac3)
While no apparent trend is observed with the 1st Serve differential, the 2nd serve differential is largest on clay, the slowest surface. 
Likely due to the fact that 2nd serves with topspin will bounce high, making the returner more likely to struggle, as opposed to grass, where the ball won't bounce nearly as much. 
Heightens the importance of a strong 2nd serve to win matches on clay. 

#### Note:
The above graphic was analysed in Python, with Shiny.


