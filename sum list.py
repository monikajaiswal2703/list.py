# a=[1,2,3,4,5,6,7,8,9]
# b=[]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+i
#     i+=1
#     b.append(sum)
# print(b)

# my_list=[1,2,3,4,5,6,7,8,9]
# i=0
# sum=0
# while i<len(my_list):
#     sum=sum+i
#     i+=1
# print(sum)

a=[2,3,2,4,5,6,4,5,7,8,5,]
i=0
b=[]
while i<len(a):
    if a[i] in b:
        print
    else:
        b.append(a[i])
    i+=1
print(b)