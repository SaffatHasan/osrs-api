from abc import ABC
from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Pool
import requests
import time


class AbstractAPI(ABC):
    def __init__(self, base_url, update_player_base_url, competition_base_url,
                 cell_selector):
        self.base_url = base_url
        self.update_player_base_url = update_player_base_url
        self.competition_base_url = competition_base_url
        self.cell_selector = cell_selector

    def update_players(self, competition_id) -> None:
        names = list(self.get_players(competition_id))
        start = time.time()
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f"Started update at {current_time}")

        with Pool(len(names)) as p:
            p.map(self.update_player_xp, names)
        end = time.time()
        elapsed = time.time() - start
        elapsed = time.strftime("%M:%S", time.gmtime(elapsed))
        print(f"Finished updating everyone after {elapsed}!")
        print(
            f"See the competition here: {self.get_competition_url(competition_id)}"
        )

    def get_players(self, competition_id) -> [str]:
        """ Returns a list of players enrolled in a particular competition

    Parameters:
    competition_id (int): ID specified by third party API
    cell_selector (str):  Selector that can be used to identify each player.
                          Typically an css class
    """
        competition_url = self.get_competition_url(competition_id)
        # Perform the request
        r = requests.get(competition_url)

        # Get all the cells with player names in them
        list_of_cells = BeautifulSoup(
            r.text, features="html5lib").select(self.cell_selector)

        return map(self.extract_name_from_element, list_of_cells)

    def extract_name_from_element(self, cell) -> str:
        """ Extracts a player name from a given cell. This is typically because websites
        tend to have the player's name as a link to be updateable
    """
        # Player name is in an anchor tag
        link = cell.find('a')

        # Extract compile
        raw_name = link.string

        # convert name to human readable
        return raw_name.replace("\xa0", " ")

    def get_competition_url(self, competition_id):
        return self.competition_base_url.format(competition_id=competition_id)

    def update_player_xp(self, name):
        if name.lower() == 'pvm fidoz':
            return
        requests.get(self.update_player_base_url.format(name=name))
