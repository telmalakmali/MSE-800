import numpy as np
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
#to get the average temperatures
print("Average Temperature is",np.mean(temperatures))
#to get the min temperature
print("Minimum Temperature is",np.min(temperatures))
#to get the max temperarture
print("Maximum Temperature is",np.max(temperatures))
#to convert the temperature to Fahrenheit
Fahrenheit= temperatures * 9/5 + 32
print("Convereted temperature to fahrenheit is",Fahrenheit)
#to identify the days where the temperature was more than 20C
Above20Ctemp= np.where(temperatures > 20)
#print("temperature more than 20C is",Above20Ctemp)
Above20temday=Above20Ctemp[0]
print("temperature more than 20C is",Above20temday)