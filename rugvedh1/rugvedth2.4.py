import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")
b=a.groupby("toss_win")["dec"].value_counts()
print("the toss decision taken  by ecah team",b)