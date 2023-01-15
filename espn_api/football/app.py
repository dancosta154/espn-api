#!/usr/bin/env python3

import argparse

import weekly_high_score as weekly_high_scores
import top_scorer as top_scorer
import playoff_payout as playoff_payout
import calculate_all_payouts as calculate_all_payouts


def handleArgs():
    parser = argparse.ArgumentParser(
        prog="ESPN API Data Parser", description="Season Recap Tool",
    )
    parser.add_argument(
        "-a",
        "--action",
        required=True,
        choices=[
            "weekly_high_scores",
            "top_scorer",
            "playoff_payouts",
            "calculate_payouts",
        ],
    )
    parser.add_argument(
        "-p",
        "--payout",
        # required=True,
        help="Set the payout amount to be calculated for weekly winners",
    )
    args = parser.parse_args()
    if args.payout:
        print()
        print(f"Payout amount set to ${args.payout}")
    return args


def main():

    args = handleArgs()

    # weekly_high_scores and top_scorer require the -p argument

    if args.action == "weekly_high_scores":
        weekly_high_scores.calculate_payouts(args.payout)
    elif args.action == "top_scorer":
        top_scorer.get_top_scorer(args.payout)
    elif args.action == "playoff_payouts":
        playoff_payout.get_playoff_payouts()
    elif args.action == "calculate_payouts":
        calculate_all_payouts.calculate_all_payouts()


main()
