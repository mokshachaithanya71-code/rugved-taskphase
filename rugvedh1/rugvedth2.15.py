import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")
for i in range(2008,2010):
    b=a[a["year"]==i]["total_runs_in_match"].sum()
    print("total number of runs socred in",i,"is",b)