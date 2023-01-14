import creds as creds
import datetime
import json

league = creds.keys()


def calculate_payouts():

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
            f"Week {week}: {max((home_high_score, home_team), (away_high_score, away_team))}"
        )
        print(f"Calculated High Score for Week {week}...")

    weekly_winners = []

    for i in range(14):
        if high_score[i].rsplit(",", 1)[1].strip(")")[2:] not in weekly_winners:
            weekly_winners.append(high_score[i].rsplit(",", 1)[1].strip(")")[2:])
        continue

    weekly_payouts = []
    payout = 10

    for i in range(len(weekly_winners)):
        sum_wins = sum(weekly_winners[i] in s for s in high_score)
        weekly_payouts.append(
            f"{weekly_winners[i]} won {sum_wins} times for a payout of ${sum_wins * payout}"
        )

    with open(
        "output/weekly_high_scores_payout_"
        + datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S")
        + ".csv",
        "w",
    ) as f:
        json.dump(weekly_payouts, f, indent=0, ensure_ascii=False)

    return
