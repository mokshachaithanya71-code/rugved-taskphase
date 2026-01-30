import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")
b=a["won_by"].mean()
c=a["won_by"].median()
d=a["won_by"].std()
print("the mean median std deviation is",b,c,d)