#pip install ucimlrepo , Installed the ucimlrepo package in https://archive.ics.uci.edu/dataset/53/iris
'''Import the dataset into your code 
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 
'''

# Import the correct function
from ucimlrepo import fetch_ucirepo #Package name: ucimlrepo , function name: fetch_ucirepo

# id=53 refers to the internal dataset number
iris = fetch_ucirepo(id=53)

# Access the feature data (X) and target labels (y), .data.features and data.targets are inbuit structed data fields
x = iris.data.features
y = iris.data.targets

# Display the first few rows of each
print("Feature data (x):")
print(x.head()) #head is a in build pandas function to show first few rows. If I give a number inside the () then it will should only that number of lines

print("\nTarget data (y):")
print(y.head())
