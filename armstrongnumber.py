b=[]
lower=int(input("enterlower range"))
upper=int(input("enter upper range"))
for i in range(lower,upper+1):
    s=0
    c=i
    while c>0:
        a=c%10
        s=s+a**3
        c=c//10
    if i==s:
        b.append(i)
print (b)


