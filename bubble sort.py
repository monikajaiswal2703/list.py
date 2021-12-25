# size=int(input("enter the size"))
# a=[]
# for i in range(size):
#     num=int(input("enter the number"))
#     a.append(num)
# for i in range(size):
#     for j in range(size-i-1):
#         if a[j]>a[j+1]:
#             t=a[j]
#             a[j]=a[j+1]
#             a[j+1]=t
#             print("sort arrey is",a)

size=int(input("enter the size"))
i=0
a=[]
while i<(size):
    num=int(input("enter the number"))
    a.append(num)
    i+=1
print(a)
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
        j+=1
    i+=1
print("sort array is",a)
