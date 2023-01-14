import creds as creds
import datetime
import json

league = creds.keys()


def get_free_agents():

    free_agents_all = league.free_agents()
    free_agents = []

    for i in range(1, len(free_agents_all)):
        fa_dict = free_agents_all[i].__dict__
        free_agents.append(
            f"ProjectedPoints: {float(fa_dict['projected_points'])}, Player: {fa_dict['name']}, Position: {fa_dict['position']}, PosRank: {fa_dict['posRank']}, InjuryStatus: {fa_dict['injuryStatus']}, PercentOwned: {fa_dict['percent_owned']}, PercentStarted: {fa_dict['percent_started']}"
        )

    free_agents = sorted(free_agents, reverse=True)

    with open(
        "output/current_free_agents_"
        + datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S")
        + ".csv",
        "w",
    ) as f:
        for line in free_agents:
            f.write(f"{line}\n")

    return
