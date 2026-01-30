import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")

b=a["tie_normal"].value_counts()
print("the total number of normal and tie matches", b)