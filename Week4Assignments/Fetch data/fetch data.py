import pandas as pd

def main():
    # Path
    filepath = "C:/Users/DELL/OneDrive/Documents/GitHub/MSE-800/Week4Assignments/Fetch data/1965__Screen_Observations__daily.csv"

    # Load 
    df = pd.read_csv(filepath)

    # Show the first 5 rows. Head is an inbuit function in python that will show the first 5 rows
    print("Preview of Data:")
    print(df.head())

    # Show missing values. isnull also is an in buuilt function that return empty values in boolean format and sum will show how many trues are there
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Show summary statistics. This inbuilt function will give the statistics like mean,min , max ,count etc for each numberic value column 
    print("\nSummary Statistics:")
    print(df.describe())

if __name__ == "__main__":
    main()