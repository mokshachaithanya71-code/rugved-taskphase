def triple_and(a,b,c):
        if a=="True" and b=="True" and c=="True":
            return True
        else:
              return False
print("enter the a and b and c")
a=input()
b=input()
c=input()
k=triple_and(a,b,c)
print(k)