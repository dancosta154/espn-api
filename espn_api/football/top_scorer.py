import creds as creds
import datetime

league = creds.keys()


def get_top_scorer(payout):
    annual_payout = int(payout)
    top_scorer = [(str(league.top_scorer()).strip("Team()"), annual_payout)]

    top_scorer = [str(x).strip("()") for x in top_scorer]

    with open(
        f"output/Season_High_Top_Scorer_Payout_{datetime.datetime.today().year - 1}.csv",
        "w",
    ) as f:
        for line in top_scorer:
            f.write(f"{line}\n")

    return print(f"{f.name.strip('/output')} has been added to the Output directory.")
