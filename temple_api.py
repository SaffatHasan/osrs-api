from abstract_api import AbstractAPI

TEMPLE_BASE_URL = "https://www.templeosrs.com/"
TEMPLE_COMPETITION_URL = f"{TEMPLE_BASE_URL}/competitions/standings.php?id=" + "{competition_id}"
TEMPLE_UPDATE_PLAYER_BASE_URL = f"{TEMPLE_BASE_URL}//php/add_datapoint.php?pvm=1&player=" + "{name}"
TEMPLE_CELL_SELECTOR = ".participant-row"


class TempleOSRSAPI(AbstractAPI):
    def __init__(self):
        super().__init__(TEMPLE_BASE_URL, TEMPLE_UPDATE_PLAYER_BASE_URL,
                         TEMPLE_COMPETITION_URL, TEMPLE_CELL_SELECTOR)
