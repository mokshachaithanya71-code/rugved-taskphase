print("enter the string")
a=input()
a=list(a)
count1=0
t=len(a)
for i in range(t,0,-1):
    k=t//i
    b=[]
    
    if t%i==0:
        count1=0
        for j in range(0,t-k):
            if a[j]==a[j+k]:
                count1=count1+1

               
        if count1==t-k and i!=1:
            print("the strig is divisible in trems of ",i)
           
            break
if(i==1):
    print("not divisible ")