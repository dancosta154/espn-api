import creds as creds
import datetime

league = creds.keys()


def get_playoff_payouts():
    # Get playoff teams

    playoff_teams = []

    for i in league.teams:
        if i.final_standing <= 4:
            playoff_teams.append((str(i).strip("Team()"), i.final_standing))

    sorted_playoffs = sorted(playoff_teams, key=lambda x: x[-1])

    # Calculate payouts
    playoff_payout = {1: 300, 2: 150, 3: 70, 4: 50}

    final_payout = []

    for k, v in playoff_payout.items():
        for i in range(4):
            if sorted_playoffs[i][1] == k:
                final_payout.append((sorted_playoffs[i][0], v))

    final_payout = [str(x).strip("()") for x in final_payout]

    with open(
        "output/Playoff_Payouts_"
        + datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S")
        + ".csv",
        "w",
    ) as f:
        for line in final_payout:
            f.write(f"{line}\n")

    return print(f"{f.name.strip('/output')} has been added to the Output directory.")
