print("enter the string")
a=input()
j=len(a)
a=list(a)
a.sort()
print("the sorted string is",a)
for i in a:
    
        p=a.count(i)
        print(i,p)