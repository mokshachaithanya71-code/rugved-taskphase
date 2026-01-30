import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")
b=a["year"].value_counts()
print(b)