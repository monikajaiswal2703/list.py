# a=[10,20,30,40,50]
# i=0
# a=10
# b=20
# a,b=b,a
# while a<a:
#     if a<a:
#         a=b[i]
#     i=i+1
# print(b)

a=[[50,40],[23,70],[56,12],[5,10,7]]
i=0
min=a[i]
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j]<min :
            min=a[i][j]
            j+=1
        i+=1
    print(min)
# i=0
# max1=0
# while i<len(a):
#     if a[i]>max1:
#         if a[i]!=max:
#             max1=a[i]
#     i+=1
# print(max1)