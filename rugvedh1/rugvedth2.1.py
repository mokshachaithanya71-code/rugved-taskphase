import csv
with open("c:\\rugvedh1\\ipl.csv","r")as file:
    a=csv.DictReader(file)
    a=list(a)
    print(a)
    
    keys1=[]
    values1=[]
    keys1=list(a[1].keys())
    print(keys1)
    for i in a:
        
            values1.append(list(i.values()))
            print(values1)
            
    count1=0
    for i in values1:
        for j in i:
            if j=='2008':
                count1=count1+1
    print("the totla number of matches in year is 2008 ",count1)