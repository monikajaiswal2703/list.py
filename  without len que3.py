# number=[50,40,23,70,56,12,5,10,7]
# count=0
# for i in number:
#     count=count+1
# print(count)

# a= int(input("enter the num"))
# b=a%10
# if a%10==b:
#  print(b,"last num")
# else:
#     print("error")

size=int(input("enter the size"))
i=0
a=[]
while i<(size):
    num=int(input("enter the number"))
    a.append(num)
    i+=1
print(a)#     print("error")
                 
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

