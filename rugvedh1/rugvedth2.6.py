import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")
b=a[a["tie_normal"]=="tie"]
print(b)