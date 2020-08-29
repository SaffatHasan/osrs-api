from temple_api import TempleOSRSAPI
import time

api = TempleOSRSAPI()

KBD_COMPETITION_ID = 2394

def main():
    api.update_players(KBD_COMPETITION_ID)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(300)
