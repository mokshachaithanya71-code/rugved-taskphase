import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")
b=a.groupby("win").value_counts()
print(b)