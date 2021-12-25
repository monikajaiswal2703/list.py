# a=[50,40,23,70,56,12,5,10,7]
# i=0
# a=70
# b=56
# a,b=b,a
# while a>a:
#     i=i+1
# print(b)

# a=[10,20,30,40,50]
# print (max(a))

a=[50,40,23,70,56,12,5,10,7]
i=0
max=0
while i<len(a):
    if a[i]>max:
     max=a[i]
    i+=1
print(max)


