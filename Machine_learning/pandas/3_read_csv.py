#Assumimg a dataframe/dataset is already present,
#this is how we read/load it

import pandas as pd
#loading id.csv into pandas dataframe
data=pd.read_csv("diabetes.csv")
print(data) #displaying the dataframe

#
print("display specific columns")
print(data['Glucose']) #displaying single column
print(data[["Glucose","BMI"]]) #displaying multiple column
#
print(data.shape) #displays shape of dataset

print(data.size) #display size of data

#INDEXING
print(data.head()) #prints first 5 rows of data
print(data.tail()) #prints last 5 rows of data