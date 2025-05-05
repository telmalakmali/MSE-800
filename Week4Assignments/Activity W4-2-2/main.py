import pandas as pd

from process_csv import CSVLoader
from process_Parquet import ParquetLoader
from process_text import TextLoader
from process_unsupported import UnsupportedLoader

class DataProcessor:
    def __init__(self, folder_path):  # Accept folder path containing all files
        self.folder_path = folder_path
        self.data = None
        self.loaders = [CSVLoader, ParquetLoader, TextLoader, UnsupportedLoader]  

    def load_data(self):
        # This method will loop over all files in the folder path
        for file_path in self.folder_path:  # You need to specify files manually in this example, file_path is a variable
            for loader in self.loaders: # loader is a variable that takes the value from the variable self.loaders list
                if loader.can_load(file_path):  #  Try to load the file using the can load function in each sub file
                    self.data = loader.load(file_path)  #  Load the data  using the load function in each sub file to read the file
                    print(f"Data loaded successfully from {file_path}")
                    return  # Exit after the first valid file is loaded

    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")
        
        print("Initial Data Summary:")
        print(self.data.info())  # Display the data summary
        print("\nMissing Values:")
        print(self.data.isnull().sum())  # Display missing values per column
        print("\nDescriptive Statistics:")
        print(self.data.describe())  # Show descriptive statistics (like mean, std, etc.)

def main():
    folder_path = [  #  List of file paths
        r'C:\Users\DELL\OneDrive\Documents\GitHub\MSE-800\Week4Assignments\Activity W4-2-2\sample_junk_mail.csv',
        r'C:\Users\DELL\OneDrive\Documents\GitHub\MSE-800\Week4Assignments\Activity W4-2-2\sample_data_2.parquet',
        r'C:\Users\DELL\OneDrive\Documents\GitHub\MSE-800\Week4Assignments\Activity W4-2-2\sample_file.text',
        r'C:\Users\DELL\OneDrive\Documents\GitHub\MSE-800\Week4Assignments\Activity W4-2-2\screenshot_1'
    ]
    processor = DataProcessor(folder_path)  #  Pass the folder path containing all files to the processor
    processor.load_data()  #  Load the data from the list of files
    processor.initial_processing()  #  Process the data if loaded successfully

if __name__ == "__main__":
    main()