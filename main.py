#!/usr/bin/python3
from cml_api import CrystalMathLabsAPI
from temple_api import TempleOSRSAPI
from config import APIConfig
import sys
from args import parse_args
import time

NUM_DAYS = 7
NUM_UPDATES = NUM_DAYS * 24 / 4

def update(api, competition_id):
    api.update_players(competition_id)

def wait(num_sec):
    print(f"Sleeping for {num_sec}s...")
    time.sleep(num_sec)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])

    api = args.api()
    competition_id = args.competition_id
    sleep_duration = args.sleep_duration

    for _ in range(int(NUM_UPDATES)):
        update(api, competition_id)
        wait(sleep_duration)
