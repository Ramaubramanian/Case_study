# Stats about V Kohli
king_df = df[df.batter == 'V Kohli']
#Runs scored by Kohli vs all bowlers
kdf1 = pd.DataFrame(king_df.groupby('bowler')['batsman_runs'].sum()).reset_index()
kdf1.head()
#Balls faced by Kohli vs all bowlers
kdf2 = pd.DataFrame(king_df.groupby('bowler')['ball'].count())
kdf2.head()
# Merging kdf1 & kdf2
kdf3 = kdf1.merge(kdf2, on='bowler', how = 'left')
kdf3.head()
kdf3['Strike_Rate'] = 100 * kdf3['batsman_runs'] / kdf3['ball']
kdf3.head()
# Sorting Index 
bdf3.reset_index(inplace=True,drop=True)
kdf3.reset_index(inplace=True,drop=True)
# Batter's SR vs Bumrah
bdf3.sort_values('Strike_Rate', ascending = False)
# Kohli's SR vs Bowlers he faced
kdf3.sort_values('Strike_Rate', ascending = False)
