# Batters vs Bumrah(min 30 balls faced)
plt.figure(figsize=(16,16))

for i in range(len(bdf3)):
    if bdf3['batter'][i] == "RR Pant":
        plt.text(bdf3['Strike_Rate'][i] - 5, bdf3['batsman_runs'][i], bdf3['batter'][i])
    else:
        plt.text(bdf3['Strike_Rate'][i] + 1, bdf3['batsman_runs'][i] - 1, bdf3['batter'][i])

plt.axvline(140, ls='--', color='red')
plt.axhline(60, ls='--', color='black')

plt.title("Batters vs Bumrah in IPL (min 30 balls faced)")
plt.xlabel("Strike Rate")
plt.ylabel("Runs scored")
plt.scatter(bdf3.Strike_Rate, bdf3.batsman_runs)
plt.show()

#Virat Kohli vs Bowlers in IPL (min 30 balls faced)
plt.figure(figsize=(18,18))

for i in range(len(kdf3)):
    plt.text(kdf3['Strike_Rate'][i] + 1, kdf3['batsman_runs'][i] - 1, kdf3['bowler'][i])

plt.axvline(130, ls='--', color='red')
plt.axhline(80, ls='--', color='black')

plt.title("Virat Kohli vs Bowlers in IPL (min 30 balls faced)")
plt.xlabel("Strike Rate")
plt.ylabel("Runs scored")
plt.scatter(kdf3.Strike_Rate, kdf3.batsman_runs)
plt.show()
