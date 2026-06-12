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
