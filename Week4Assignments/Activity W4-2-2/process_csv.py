import pandas as pd

class CSVLoader:
    @staticmethod
    def can_load(file_path):
        return file_path.lower().endswith('.csv')

    @staticmethod
    def load(file_path):
        return pd.read_csv(file_path)