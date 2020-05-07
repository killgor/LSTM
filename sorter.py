import pandas as pd

# load dataset
df = pd.read_csv('data1mpredict.csv',sep=',', header=0, index_col=0, squeeze=True)


df.sort_values(by='Time(UTC)', inplace=True,)

df.info()
df.head()
df.to_csv('data1mtarget.csv', index='Time(UTC)')
