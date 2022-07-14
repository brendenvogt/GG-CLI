
import json
import os
from pathlib import Path
from ggcli import PACKAGE_ROOT

DATA_PATH = "data"


class Loader():

    def __init__(self, data_path=None, file_loader=None) -> None:
        self.data_path = data_path
        if self.data_path == None:
            self.data_path = DATA_PATH

        self.file_loader = file_loader
        if self.file_loader == None:
            self.file_loader = JSONFileLoader()

    def load_data(self, file_name):
        return self.file_loader.load_data(file_name)


class JSONFileLoader(Loader):

    def __init__(self, data_path=None) -> None:
        super().__init__(data_path, self)

    def load_data(self, file_name):
        file_path = Path(file_name).with_suffix(".json")
        full_path = os.path.join(PACKAGE_ROOT, self.data_path, file_path)
        data = None
        with open(full_path) as f:
            data = json.load(f)
        return data
