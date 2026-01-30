print("enter the string")
a=input()
a=list(a)
print(a)
t=len(a)
for i in range(0,t-1):
    min=i
    for j in range(i+1,t):
        if a[j]<a[min]:
            min=j
    temp=a[min]
    a[min]=a[i]
    a[i]=temp
print("the sorted string is ",a)