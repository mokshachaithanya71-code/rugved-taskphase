import csv
with open("c:\\rugvedh1\\ipl.csv","r")as file:
    a=csv.reader(file)
    b=list(a)
    count1=0
    count2=0
    count3=0
    count4=0
    print(b)
    k=[]
    for i in b:
        
            if i[0]=="2008":
                if i[8]=="hyd":
                    count1=count1+1
                if i[8]=="del":
                    count2=count2+1
                if i[8]=="che":
                    count3=count3+1
                if i[8]=="ben":
                    count4=count4+1
    d={
        "hyd":0,
        "del":0,
        "che":0,
        "ben":0
    }
    d["hyd"]=count1
    d["del"]=count2
    d["che"]=count3
    d["ben"]=count4
    print(d)
    c=[]
    c=list(d.values())
    w=len(c)
    c.sort(reverse=True)
    h=c[0]
    q=c[w-1]
    for s in d:
        if d[s]==h:
             print(" the  city where the most team won is ",s)
        if d[s]==q:
             print("the city where the mostt team lost is ",s)
    