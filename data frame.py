import numpy as np
import pandas as pd
arr=np.array([[2,12,3,7],[3,11,4,5],[5,18,7,9]])
col=['Eleanor','chidi','tahani','jason']
df=pd.DataFrame(data=arr,columns=col)
print(df)
print('\n\t',df['Eleanor'].iloc[1])
df['Janet']=df['tahani']+df['jason']
print('\n',df)


