def rec(a):
    if a==1:
        return 1
    else:
        return a*rec(a-1)
print("enter the number")
a=int(input())
t=rec(a)
print("the factriol is",t)