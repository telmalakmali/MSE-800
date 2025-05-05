import pandas as pd

class UnsupportedLoader:
    @staticmethod
    def can_load(file_path):
        return True  # Catch-all loader for unsupported formats

    @staticmethod
    def load(file_path):
        raise ValueError("Unsupported file format. Please use CSV or Parquet.")