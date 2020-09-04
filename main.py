from cml_api import CrystalMathLabsAPI
import time

api = CrystalMathLabsAPI()

RC_COMPETITION_ID = 27821

def main():
    api.update_players(RC_COMPETITION_ID)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(300)
