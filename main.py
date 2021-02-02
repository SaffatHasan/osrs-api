#!/usr/bin/python3
from cml_api import CrystalMathLabsAPI
from temple_api import TempleOSRSAPI
from config import APIConfig
import time

config = APIConfig()
api = config.get_api()

NUM_DAYS = 7
NUM_UPDATES = NUM_DAYS * 24 / 4

def update():
    competition_id = config.get_competition()
    api.update_players(competition_id)

def wait():
    num_sec = config.sleep_duration
    print(f"Sleeping for {num_sec}s...")
    time.sleep(num_sec)

if __name__ == "__main__":
    for _ in range(int(NUM_UPDATES)):
        update()
        wait()
