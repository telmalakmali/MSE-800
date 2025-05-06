import pandas as pd

#read_parquet is an inbuilt function in the Pandas library. It is used to read Parquet files
df = pd.read_parquet(r'C:\Users\DELL\OneDrive\Documents\GitHub\MSE-800\Week4Assignments\Big_data_with_Parquet\Sample_1m.parquet') 
print(len(df)) #len(df) is inbuilt python function that returns the number of rows