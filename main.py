#!/usr/bin/python3
from cml_api import CrystalMathLabsAPI
from temple_api import TempleOSRSAPI
from config import APIConfig
import time

config = APIConfig()
api = config.get_api()

NUM_DAYS = 7
NUM_UPDATES = NUM_DAYS * 24 / 4

def main():
    competition_id = config.get_competition()
    api.update_players(competition_id)

if __name__ == "__main__":
    for _ in range(int(NUM_UPDATES)):
        main()
        num_mins = 15
        num_sec = num_mins * 60
        print(f"Sleeping for {num_sec}s...")
        time.sleep(num_sec)
