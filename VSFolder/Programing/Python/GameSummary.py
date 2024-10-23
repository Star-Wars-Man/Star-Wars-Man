def showSummary(title, date, home_team, score_home, score_away):
#    games_won =  win_rate / 100 * games_played
#    games_played = 1 + games_played
    print("")
    was_a_win = score_home > score_away
    was_a_tie = score_home == score_away
    print(f"Game: {title} ({date})")
    print("---------------------------")
    if was_a_win == True:
#        games_won = games_won + 1
#        win_rate = games_won / games_played * 100
        print(f"{home_team} won: {score_home} - {score_away}")
#        print(f"win rate: {win_rate}%")
    elif was_a_tie == True:
#        win_rate = games_won / games_played * 100
        print(f"{home_team} Tied")
#        print(f"{win_rate}% ")
    else:
#        win_rate = games_won / games_played * 100
        print(f"{home_team} lost: {score_away} - {score_home}")
#        print(f"{win_rate}% ")
    print("")
def exportSummary(fileName, stuf):
    fileName = fileName + ".txt"
    new = open(fileName,"x")
    new.write(stuf)
f = open("./Programing/Python/pickle.txt","r")
file = f.read()
line = file.strip().splitlines()
x = 1
while x <= 149:
    l1 = line[x].strip().split(",")
    showSummary(l1[0],l1[1],l1[2],l1[3],l1[4])
    x += 1