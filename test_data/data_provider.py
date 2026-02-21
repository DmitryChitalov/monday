import json


class DataProvider:
    def __init__(self, file_name):
        with open(file_name, encoding='utf-8') as file_name:
            self.data = json.load(file_name)

    def get(self, key):
        return self.data.get(key)
