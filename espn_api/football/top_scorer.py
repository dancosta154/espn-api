import creds as creds
import datetime

league = creds.keys()


def get_top_scorer(payout):
    annual_payout = int(payout)
    top_scorer = (
        f'{str(league.top_scorer()).strip("Team()")} earned ${int(annual_payout)}.'
    )

    with open(
        "output/Season_High_Top_Scorer"
        + datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S")
        + ".csv",
        "w",
    ) as f:
        f.write(top_scorer)

    return print(f"{f.name.strip('/output')} has been added to the Output directory.")
