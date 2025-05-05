import pandas as pd

class ParquetLoader:
    @staticmethod
    def can_load(file_path):
        return file_path.lower().endswith('.parquet')

    @staticmethod
    def load(file_path):
        return pd.read_parquet(file_path)