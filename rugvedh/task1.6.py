print("enter the strings ")
a=input()
b=input()
a=list(a)
b=list(b)
c=[]

if len(a)==len(b):
    if sorted(a)==sorted(b):
        print("the strings are anagram")
    else:
        print("strings are not angram")

