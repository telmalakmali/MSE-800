import pandas as pd
file_path = 'C:/Users/DELL/OneDrive/Documents/GitHub/MSE-800/Week4Assignments/sample_text.txt'
df = pd.read_csv(file_path)
print(df.head())
print(open(file_path).read().count('__'))

#Correct function to read Parquet file
file_path = 'C:/Users/DELL/OneDrive/Documents/GitHub/MSE-800/Week4Assignments/Sample_data_2.parquet'
df1 = pd.read_parquet(file_path)
# Show first 5 rows
#print(df.head())
features = df1.shape
# Print number of features (columns)
print("Number of features:", features)