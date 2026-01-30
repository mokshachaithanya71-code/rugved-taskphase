import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")
for i in range(2008,2010):
    b=a[a["year"]==i]
    c=b.groupby("toss_win")["dec"].value_counts()
    print("the decicion took by team won in toos in ",i,"is",c)