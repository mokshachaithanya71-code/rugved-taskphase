import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")
b=a["umpire"].max()
print("more number of times umpire ",b)
c=a.loc[a["umpire"]==b]
print(c)