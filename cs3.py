### Info req: Runs scored, Balls Faced, No.of times dissmised
req_df.batsman_runs
#runs Scored by Kohli vs Bumrah
sum(req_df.batsman_runs)
#balls faced by Kohli vs Bumrah
len(req_df)
#Bumrah dismised Kohli
req_df[req_df.player_dismissed == 'V Kohli']
len(req_df[req_df.player_dismissed == 'V Kohli'])
#SR
100 * (sum(req_df.batsman_runs)/len(req_df))
#Stats about Bumrah
fb_god = df[df.bowler == 'JJ Bumrah']
fb_god.head(10)
bdf1 = pd.DataFrame(fb_god.groupby('batter')['batsman_runs'].sum()).reset_index()
bdf2 = pd.DataFrame(fb_god.groupby('batter')['ball'].count())
#Merging other batter's record vs Bumrah
bdf3 = bdf1.merge(bdf2, on = 'batter', how = 'left')
bdf3.head(5)
#Adding Strike rate columns
bdf3['Strike_Rate'] = 100*bdf3['batsman_runs']/bdf3['ball']
bdf3 = bdf3.drop(columns=['Strike Rate'])
bdf3.head(1)
#Min criteria: 30 balls
bdf3 = bdf3[bdf3.ball >= 30]
bdf3.head()
