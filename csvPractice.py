import csv

with open('wc_2026_fixtures.csv', 'r') as file:
    csv_read = csv.DictReader(file)

    # for line in csv_read:
    #     if(line['team1'] == 'Argentina' or line['team2'] == 'Argentina'):
    #         print(line['team1'], " vs ", line['team2'], " - ", line['date'])

    fields = ['date', 'team1', 'team2', 'venue']
    with open('argentina.csv', 'w') as newF:
        writer = csv.DictWriter(newF, fieldnames=fields)
        writer.writeheader()
        for line in csv_read:
            if(line['team1'] == 'Argentina' or line['team2'] == 'Argentina'):
                writer.writerow(line)

print('\nNext\n')

with open("wc_2026_fixtures.csv", "r") as file:
    csv_read = list(csv.DictReader(file))
    usa_c, mex_c, can_c = 0, 0, 0
    for line in csv_read:
        if(line['country'] == 'Mexico'):
            mex_c += 1
        elif(line['country'] == 'USA'):
            usa_c += 1
        else:
            can_c += 1

    print("USA: ", usa_c)
    print("Mexico: ", mex_c)
    print("Canada: ", can_c)

    print("\nNext\n")

    mini = float('inf')
    best_team = ''
    best_coach = ''
    for line in csv_read:
        if not line['team1_fifa_rank']:
            continue

        team1 = int(line['team1_fifa_rank'])
        team2 = int(line['team2_fifa_rank'])
        if(team1 < mini):
            mini = team1
            best_team = line['team1']
            best_coach = line['team1_coach']
        if(team2 < mini):
            mini = team2
            best_team = line["team2"]
            best_coach = line["team2_coach"]
    print(f"Team: {best_team}, Coach: {best_coach}, Rank: {mini}")

    print("\nNext\n")

    coach_count = {}

    for line in csv_read:
        if line['stage'] != 'Group Stage':
            continue
        coach1 = line["team1_coach"]
        coach2= line["team2_coach"]

        if coach1 not in coach_count:
            coach_count[coach1] = 0
        if coach2 not in coach_count:
            coach_count[coach2] = 0

        coach_count[coach1] += 1
        coach_count[coach2] += 1

    print(coach_count)

print("\nNext\n")

with open('wc_all_matches.csv', 'r', encoding='utf-8') as all_matches:
    matches = list(csv.DictReader(all_matches))

    wins = {}

    for match in matches:
        if int(match['score1']) > int(match['score2']):
            teamA = match['team1']
            if teamA not in wins:
                wins[teamA] = 0
            wins[teamA] += 1
        elif int(match["score2"]) > int(match["score1"]):
            teamB = match["team2"]
            if teamB not in wins:
                wins[teamB] = 0
            wins[teamB] += 1

    print(sorted(wins.items(),key= lambda item: item[1] , reverse=True))
    # print(wins)
    with open('all_teams_wins.csv', 'w') as winsT:
        writer = csv.DictWriter(winsT, fieldnames=['team','wins'])
        writer.writeheader()

        for team, win_c in sorted(wins.items(), key=lambda item: item[1], reverse=True):
            writer.writerow({
                'team': team,
                'wins': win_c
            }
            )

    teamA = ''
    teamB = ''
    year = ''
    teamASc = 0
    teamBSc = 0
    total_G = float('-inf')   # or simply 0 bc no match will have less than 0

    for match in matches:
        totSc = int(match['score1']) + int(match['score2'])
        if totSc > total_G:
            teamA = match['team1']
            teamB = match['team2']
            year = match['year']
            teamBSc = int(match["score2"])
            teamASc = int(match['score1'])
            total_G = totSc

    print('\n' + teamA + ' ' + str(teamASc) + ' - ' + str(teamBSc) + ' ' + teamB)
    print(f'Total Goals: {total_G}')
    print(f'Year: {year}')

    print("\nNext\n")

    hosts = {}

    for match in matches:
        hosts[match['country']] = hosts.get(match['country'], 0) + 1

    print(sorted(hosts.items(), key = lambda item: item[1], reverse=True))

    print("\nNext\n")

    with open('finals.csv', 'w') as final:
        fields = ['year', 'team1', 'score1', 'score2', 'team2', 'winner']
        writer2 = csv.DictWriter(final, fieldnames=fields)

        writer2.writeheader()
        for match in matches:
            if match['stage'] == 'Final':
                if int(match['score1']) > int(match['score2']):
                    winner = match['team1']
                elif int(match['score1']) < int(match['score2']):
                    winner = match['team2']
                else:
                    winner = 'TIE'
                writer2.writerow({
                    'year': match['year'],
                    'team1': match['team1'],
                    'score1': match['score1'],
                    'score2': match['score2'],
                    'team2': match['team2'],
                    'winner': winner
                })

    with open("team_stats.csv", "w") as final:
        fields = ["team", "matches_played", "wins", "losses", "goals_scored", "goals_conceded"]
        writer3 = csv.DictWriter(final, fieldnames=fields)

        writer3.writeheader()

        teams = {}

        for match in matches:
            teamA = match['team1']
            teamB = match['team2']

            if teamA not in teams:
                teams[teamA] = {
                    # 'team': teamA,
                    'matches_played': 0,
                    'wins': 0,
                    'losses': 0,
                    'goals_scored': 0,
                    'goals_conceded': 0
                }
            if teamB not in teams:
                teams[teamB] = {
                    # "team": teamB,
                    "matches_played": 0,
                    "wins": 0,
                    "losses": 0,
                    "goals_scored": 0,
                    "goals_conceded": 0,
                }

            teams[teamA]["matches_played"] += 1
            teams[teamB]["matches_played"] += 1

            if int(match['score1']) > int(match['score2']):
                teams[teamA]["wins"] += 1
                teams[teamB]["losses"] += 1
            elif int(match["score1"]) < int(match["score2"]):
                teams[teamB]["wins"] += 1
                teams[teamA]["losses"] += 1

            teams[teamA]["goals_scored"] += int(match["score1"])
            teams[teamB]["goals_conceded"] += int(match["score1"])
            teams[teamB]["goals_scored"] += int(match["score2"])
            teams[teamA]["goals_conceded"] += int(match["score2"])

        print(teams)

        for team, stats in teams.items():
            writer3.writerow(
                {
                    "team": team,
                    "matches_played": stats["matches_played"],
                    "wins": stats["wins"],
                    "losses": stats["losses"],
                    "goals_scored": stats["goals_scored"],
                    "goals_conceded": stats["goals_conceded"],
                }
            )
