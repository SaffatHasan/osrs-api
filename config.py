import yaml
from cml_api import CrystalMathLabsAPI
from temple_api import TempleOSRSAPI

DEFAULT_CONFIG_PATH="config.yml"

class APIConfig:
    def __init__(self):
        self.config = self.load_config()


    def load_config(self):
        with open(DEFAULT_CONFIG_PATH, 'r') as f:
            return yaml.safe_load(f)

    def get_api(self):
        type_map = {
                TempleOSRSAPI.identifier: lambda: TempleOSRSAPI(),
                CrystalMathLabsAPI.identifier: lambda: CrystalMathLabsAPI(),
                }

        return type_map[self.config['type']]()

    def get_competition(self):
        return self.config['competition']



