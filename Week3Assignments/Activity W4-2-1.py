import pandas as pd
file_path = '/content/drive/MyDrive/Colab Notebooks/sample_text.txt'
df = pd.read_csv(file_path)
print(df.head())
print(open(file_path).read().count('__'))

#Correct function to read Parquet file
df = pd.read_parquet(file_path)
# Show first 5 rows
#print(df.head())
features = df.shape
# Print number of features (columns)
print("Number of features:", features)