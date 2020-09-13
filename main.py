from cml_api import CrystalMathLabsAPI
import time

api = CrystalMathLabsAPI()

RC_COMPETITION_ID = 27915

def main():
    api.update_players(RC_COMPETITION_ID)

if __name__ == "__main__":
    while True:
        main()
        num_mins = 15
        num_sec = num_mins * 60
        time.sleep(num_sec)
