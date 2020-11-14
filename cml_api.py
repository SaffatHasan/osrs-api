from abstract_api import AbstractAPI

CML_BASE_URL = "https://www.crystalmathlabs.com/tracker"
CML_COMPETITION_URL = f"{CML_BASE_URL}/competitions.php?competition=" + "{competition_id}"
CML_UPDATE_PLAYER_BASE_URL = f"{CML_BASE_URL}/update.php?player=" + "{name}"
CML_CELL_SELECTOR = ".hiscore_name"


class CrystalMathLabsAPI(AbstractAPI):
    identifier = 'cml'
    def __init__(self):
        super().__init__(CML_BASE_URL, CML_UPDATE_PLAYER_BASE_URL,
                         CML_COMPETITION_URL, CML_CELL_SELECTOR)
