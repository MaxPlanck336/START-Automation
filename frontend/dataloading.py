import pandas as pd

class DataLoader:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.data_path)