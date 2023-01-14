#!/usr/bin/env python3

import argparse
import textwrap

import weekly_high_score as weekly_high_scores
import free_agents as current_free_agents
import top_scorer as top_scorer


def handleArgs():
    parser = argparse.ArgumentParser(
        prog="ESPN API Data Parser",
        description="Season Recap Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-a", "--action", required=True, choices=["weekly_high_scores", "free_agents"]
    )
    parser.add_argument(
        "-p",
        "--payout",
        help="Set the payout amount to be calculated for weekly winners",
    )
    parser.add_argument("-t", "--top_scorer")
    parser.print_help()
    args = parser.parse_args()
    if args.payout:
        print()
        print(f"Payout amount set to ${args.payout}")
    return args


def main():

    args = handleArgs()

    if args.action == "weekly_high_scores":
        weekly_high_scores.calculate_payouts(args.payout)
    elif args.action == "free_agents":
        current_free_agents.get_free_agents()
    elif args.action == "top_scorer":
        top_scorer.get_top_scorer()


main()
