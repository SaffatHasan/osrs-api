import os

class APIConfig:
    def __init__(self, args):
        self.args = args

    def get_api(self):
        return self.args.api()

    def get_competition(self):
        return self.args.competition_id

    def get_sleep_duration(self):
        return self.args.sleep_duration



