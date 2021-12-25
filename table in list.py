num=int(input("enter the table number:")) 
i=1
a=[]
while i<=num:
    count=1
    while count<=10:
        p=i*count
        a.append(p)
        # print(i,"*",count,"=",p)
        count+=1
    # print()
    i+=1

print(a)
# print()