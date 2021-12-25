# num=[2,3,45,56,78,76,]
a=[50,40,23,70,56,12,5,10,7]
i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i+=1
i=0
max1=0
while i<len(a):
    if a[i]>max1:
        if a[i]!=max:
            max1=a[i]
    i+=1
i=0
max3=0
while i<len(a):
    if a[i]>max3:
        if a[i]!=max1 and a[i]!=max:
                max3=a[i]
    i+=1
print(max3)