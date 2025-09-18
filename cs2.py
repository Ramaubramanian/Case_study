#Step 2
#In this step, we are going to filter the Players from their respective teams
df.inning.unique()
#OP: array([1, 2, 3, 4, 5, 6]) where 1: 1st innings 2: 2nd innings 3: super over 1st innings 4: super over 2nd innings 5: consecutive superover 1st innings 6: consecutive superover 2nd innings
#We ignore superover innings in this case
df = df[(df.inning==1) | (df.inning==2)]
# To see all the teams in the dataset
df.bowling_team.unique()
""""OP:array(['Royal Challengers Bangalore', 'Kolkata Knight Riders',
       'Kings XI Punjab', 'Chennai Super Kings', 'Delhi Daredevils',
       'Rajasthan Royals', 'Mumbai Indians', 'Deccan Chargers',
       'Kochi Tuskers Kerala', 'Pune Warriors', 'Sunrisers Hyderabad',
       'Rising Pune Supergiants', 'Gujarat Lions',
       'Rising Pune Supergiant', 'Delhi Capitals', 'Punjab Kings',
       'Gujarat Titans', 'Lucknow Super Giants',
       'Royal Challengers Bengaluru'], dtype=object)""""
#Filtering teams to select Bumrah & Kohli stats
df[df.bowling_team == 'Mumbai Indians']['bowler'].unique()
df[df.batting_team == 'Royal Challengers Bangalore']['batter'].unique()
# Filtering Kohli and Bumrah from their respective team
req_df = df[(df.batter == 'V Kohli') & (df.bowler == 'JJ Bumrah')]
req_df.tail()
# Check unique batters
print(req_df['batter'].unique()[:20])

# Check unique bowlers
print(req_df['bowler'].unique()[:20])

# See if 'V Kohli' exists
print((req_df['batter'] == 'V Kohli').sum())

# See if 'JJ Bumrah' exists
print((req_df['bowler'] == 'JJ Bumrah').sum())
