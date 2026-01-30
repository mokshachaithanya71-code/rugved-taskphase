def fib(a):
    if a==1:
        return 1
    elif a==0:
        return 0
    else:
        return fib(a-1) + fib(a-2)
print("enter the number ")
a=int(input())
for i in range(0,a):
    t=fib(i)
    print(t)