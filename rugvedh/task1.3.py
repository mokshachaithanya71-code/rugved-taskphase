print("enter the number")
a=list(map(int,input().split()))
count1=0
for i in range(len(a)-1):
    if a[0]==a[len(a)-1]:
        if a[i]<a[i+1]:
            count1=count1+1
        if a[i]>a[i+1]:
            break
print(count1)
count2=0
for j in range(count1,len(a)-1):
    if a[j]>a[j+1]:
        count2=count2+1
print(count2)
if count2+1==len(a)-count1:
    print("the given number is hill nuber")
else:
    print("the given number is not hill number")

