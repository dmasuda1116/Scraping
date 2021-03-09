import json


class Config:
    def __init__(self, json_path="../json/config.json"):
        config = json.load(open(json_path, "r"))
        self.access_token = config["access_token"]
        self.driver_path = config["driver_path"]
