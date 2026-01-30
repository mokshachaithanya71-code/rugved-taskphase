import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")
b=a.groupby("city")["total_runs_in_match"].value_counts()
print(b)
c=a.groupby("city")["total_runs_in_match"].mean()
print(c)