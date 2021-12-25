x=int(input("enter number:-"))
a=0
b=x
total=0
while(b>0):
    a=b%10
    fact=1
    while(a):
        fact=fact*a
        a=a-1
    total=total+fact
    b=b//10
if (total==x):
     print(x,"strong number")
else:
    print(x,"not strong number")
