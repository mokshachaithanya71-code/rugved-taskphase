import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")
c=a["won_by"].max()
b=a.loc[a["won_by"].idxmax(),"win"]
print(c)
print(b)
print(a.loc[a["won_by"]==c])
