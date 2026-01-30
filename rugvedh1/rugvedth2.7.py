import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")
b=a.loc[a["won_by"].idxmax(),"win"]
c=a["won_by"].max()
print(b)
print(c)
t=a.loc[a["won_by"].idxmin(),"win"]
r=a["won_by"].min()
print(t)
print(r)
