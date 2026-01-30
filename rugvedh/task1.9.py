print("enter the string")
a=input()
print("enter how many times each character should be shifted")
n=int(input())
l=len(a)
a=list(a)
for i in range(0,l):
    if a[i].isalpha():
        a[i]=chr(ord(a[i])+n)
s="".join(a)
print(s)