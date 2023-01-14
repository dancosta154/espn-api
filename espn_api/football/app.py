#!/usr/bin/env python3

import argparse

import weekly_high_score as weekly_high_scores
import free_agents as current_free_agents


def handleArgs():
    parser = argparse.ArgumentParser(description="ESPN API Data Parser")
    parser.add_argument(
        "-a", "--action", required=True, choices=["weekly_high_scores", "free_agents"]
    )
    args = parser.parse_args()
    return args


def main():

    args = handleArgs()

    if args.action == "weekly_high_scores":
        weekly_high_scores.calculate_payouts()
    if args.action == "free_agents":
        current_free_agents.get_free_agents()


main()
