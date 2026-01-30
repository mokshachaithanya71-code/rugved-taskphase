import pandas as pd
a=pd.read_csv("c:\\rugvedh1\\ipl.csv")
b=a["man_of_match"].value_counts()
print(b[b>=3])
