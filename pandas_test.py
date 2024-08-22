import pandas as pd
csize=10
file1=pd.read_csv("E:/github/python/large_dataset_with_consistent_types.csv",chunksize=csize,delimiter=',')

colList=['Name','Age']

for i in file1:
  print(i[colList])