"remove 000 in list"
a=[10,22000,13000,447000,100,1230000]
i=0
c=[]
while i<len(a):
    while a[i]>0:
        if a[i]%10!=0:
            c.append(a[i])
            break
        a[i]//=10
    i+=1
print(c)
