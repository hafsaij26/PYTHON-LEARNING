import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
#print 1st 5 rows
print(df.head())
#now tail
print(df.tail())
#rows and columns
print(df.shape)
