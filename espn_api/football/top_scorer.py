import creds as creds
import datetime
import json

league = creds.keys()


def get_top_scorer():
    return league.top_scorer()
