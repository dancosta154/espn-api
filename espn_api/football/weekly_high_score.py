import creds as creds
import datetime
import json

league = creds.keys()


def calculate_payouts(payout):

    matchup_count = int(len(league.teams) / 2)
    home_high_score = 0
    away_high_score = 0
    high_score = []

    for week in range(1, 15):
        home_high_score = 0
        away_high_score = 0

        for i in range(matchup_count):
            if league.box_scores(week)[i].home_score > home_high_score:
                home_high_score = league.box_scores(week)[i].home_score
                home_team = str(league.box_scores(week)[i].home_team).strip("Team()")
            if league.box_scores(week)[i].away_score > away_high_score:
                away_high_score = league.box_scores(week)[i].away_score
                away_team = str(league.box_scores(week)[i].away_team).strip("Team()")
        high_score.append(
            max((home_high_score, home_team), (away_high_score, away_team))
        )
        print(f"Calculated High Score for Week {week}...")

    weekly_winners = []

    for i in range(14):
        if high_score[i][1] not in weekly_winners:
            weekly_winners.append(high_score[i][1])
        continue

    weekly_payouts = []
    payout = int(payout)

    for i in range(len(weekly_winners)):
        sum_wins = sum(weekly_winners[i] in s for s in high_score)
        weekly_payouts.append((weekly_winners[i], sum_wins * payout))

    weekly_payouts = sorted(
        [str(x).strip("()") for x in weekly_payouts], key=lambda x: x[-1]
    )

    with open(
        f"output/Weekly_High_Score_Payouts_{datetime.datetime.today().year - 1}.csv",
        "w",
    ) as f:
        for line in weekly_payouts:
            f.write(f"{line}\n")

    return print(f"{f.name.strip('/output')} has been added to the Output directory.")
