import pandas as pd

df=pd.read_csv('data.csv') #loading the dataset
print('[info] data loaded successfully...')

print('[info] checking for NAN values....')
print(df.columns[df.isna().any()])

print('[info] removing NAN values...')
df=df.dropna()#this line remove entire row which nan value

print('[info] checking for Nan values again....')
print(df.columns[df.isna().any()])


