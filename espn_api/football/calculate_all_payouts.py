import creds as creds
import glob
import pandas as pd
import datetime

league = creds.keys()


def calculate_all_payouts():

    df1 = pd.read_csv(glob.glob("./output/Playoff_Payouts*")[0], header=None)
    df2 = pd.read_csv(glob.glob("./output/Season_High_Top_Scorer*")[0], header=None)
    df3 = pd.read_csv(glob.glob("./output/Weekly_High_Score*")[0], header=None)

    df = pd.concat([df1, df2, df3])
    df.rename({0: "Team", 1: "Amount Owed"}, axis=1, inplace=True)
    df["Amount Owed"] = df["Amount Owed"].astype("int")

    df_pivot = pd.pivot_table(df, values="Amount Owed", index="Team", aggfunc="sum")
    df_pivot.reset_index(inplace=True)
    df_pivot.sort_values("Amount Owed", ascending=False)

    df_pivot.to_csv(
        f"./output/{datetime.datetime.today().year - 1}_Fantasy_Football_Payouts.csv",
        encoding="utf-8",
        index=False,
    )

    return print(
        f"{datetime.datetime.today().year - 1}_Fantasy_Football_Payouts.csv has been added to the Output directory."
    )

