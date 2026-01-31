# Frisbee Model
This is a data science model that is used to analyze and compare ultimate frisbee players in the Ultimate Frisbee Association League, or UFA. These players play on different teams in the UFA at different positions. The data is found on the UFA [website](https://watchufa.com/stats/player-stats?year=2023).
## Hypothesis
Before developing this model, the expectation of it was that the New York Empire would be seen as the consensus number one team while also having may of the best players. This is due to them going undefeated in the 2023 season, including their 7 point victory in the finals over the Salt Lake Shred. 
## Process
Using different data science tools and mathematically techniques in python, the mode evaluates the players and gives them a 'score' that is eventually used to see who is the best player in the season. 
### Organization
The way the files folders are organized are different than other projects. The bigger the number, the later in the process the file was created. The folder and files are separated by major steps in the design process to allow for a backup file to be there in case of a major problem that happened when creating the model. 
### Math
Many different path concepts are used in this process to allow for the best outcomes to be shown. Some of the concepts include standardization, shrinking, and linear regression. 
#### Possessions
Before adjusting any of the numbers, every stat being measured must be a percentage, meaning the model is not judging a player on the amount of goals in the season, for example, but the chance of a goal happening during a possession. Every stat for every player was divided by the amount of times a player was on the field. 
#### Shrinking
The stats couldn't all be combined together into a number because they are not all on the same scale. To do this, every player's stats were compared to the league average of the specific stat. For example, if the league average percent of scoring a goal was 5%, someone with a goal scoring percent of 10%, they would be twice as high as anyone around 5%. 
#### Standardizing
After shrinking all the stats, the new 'adjusted' stats were then turned into ZScores which is comparing every player to everyone directly in each stat. This is where the great players started to separate themselves from the below average ones. 
#### Linear Regression
To find the final value, whatever Zscores must be multiplied by an individual weight to determine how important a stat is someone's overall value. This is where lots of bias can be found because if a human were to create the weights, they have all the power to control who is perceived as a good player, and who isn't. If someone only likes flashly player and only values goal scoring, he or she can make goals have the value 80% higher than any other stat. Instead of this possibility of bias, linear regression is used to mathematically determine the weights, so the bias is limited. Many different Zscores are put through the regression in relationship to a Zscore of offensive efficiency which is the teams' scores / offensive possesion with at least 100 possessions. 
#### Combining
After that, the score is found by multiplying the weights by the Zscores. The final step was to multiple that score an equation of minutes played to limit those players who have not played for much of the season. 
## Results
The results of the model were a little surprising due to the dominance that the New York Empire had on the league. They did rank highly, but other teams appear that they should be done even better. 
### Best Players
Only 7 players got a score above 2 out of the 460 players in the league who were: Jordan Kerr, Brandon Van Deusen, Jacob Miller, Ryan Osgar, Walker Frankenberg, Pawel Janas, and Austin Taylor. These 7 players who rated as the best players in the league due to their high offensive output and their high efficiency to score. The most interesting trend of these players is that all of them have an about 95 Completion Percentage, and 6 out of the 7 of them would be labeled as handlers, meaning they are the throwing point guard leaders of their teams. 
![Best Players](5%20Defensive/Best_Players.png)
#### Why Jordan
Jordan Kerr passed the eye test of being the best player in the league. The first note is that he scored the most points, played every game, and had the highest plus/minus stats compared to all players in the league. He was a player who was a talented thrower, with the athleticism that scared all teams; his athleticism, seen in his goal totals, would imply he only plays in a cutter role, but his limited turns show that he is not afraid of the disc being in his hand. He will be continue to lead the Shred and the league in points played because of his ability to play positionlessly on any team he plays for. 
### Best Teams
After running this model, the best team in the 2023 UFA was found to be the Salt Lake Shred. Despite the results of the season where the New York Empire went undefeated to the championship, the runner up of the league was 10% statistically better than one of the most dominate teams in their dynasty. One reason this might be is due to some of the dominate players on the New York Empire were punished due to the model's harsh punishments to turnovers. Ryan Osgar, the Empire's best player, is one of the best throwers in the league, which explains why his score is so high; however, his fellow handler, Jack Williams, could be argued as a better player than him, but he is known for taking more risks than Ryan, which takes points away from him. Another reason could also be the Shred having much more of a balanced team, due to more players doing more. The Empire did have many role players on their team, but without Ryan Osgar, the team would struggle to be offensively efficient. If you take Jordan Kerr away from the Shred, it would be difficult, but it would be the same because of Ryan's ability to throw with such accuracy, shown by his Huck%. 
### Team Comparisons
![Team Average Scores](5%20Defensive/team_avg_chart.png)
## What Next
This model does a good job in showing some of the great talent in the UFA. Two things that the best players exhibit are a scoring ability, whether that is goals or assists, and the ability to not turn the disk over. 
After creating this model, there is many changes that need to be made to value other abilities on the field. There are still many players who are good players and trusted by teams that are rated as average players, meaning there are other ways to show their talent using the on-field statistics. 
Many of the players who are rated highly in this model are offensive handlers, meaning they don't play many D-Points (Points starting on defense) and they usually are the players with high completion rates, meaning they score a high volume of their own team's points. 
Also, this model heavily favors offensive players compared to defensive players. 
## Author
Nicholas Guillet, a Junior Computer Engineer at Villanova University and advid ultimate frisbee fan. 
