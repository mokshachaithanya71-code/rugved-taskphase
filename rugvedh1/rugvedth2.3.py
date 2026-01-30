import pandas as pd
df=pd.read_csv("c:\\rugvedh1\\ipl.csv")
print(df)
a=df["city"].value_counts()
print("the totoal number of matches citywise are",a)

   